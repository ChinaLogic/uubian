import tensorflow as tf  
from os import listdir
from numpy import *
import pickle
from tensorflow.contrib.keras.python.keras.utils.np_utils import to_categorical

def weight_variable(shape):  
    initial = tf.truncated_normal(shape,stddev=0.1)  
    return tf.Variable(initial)  
def bias_variable(shape):  
    initial = tf.constant(0.1,shape=shape)  
    return tf.Variable(initial)  
def conv2d(x,W):  
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding="SAME")
def max_pool_2x2(x):  
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

def creatCNN(traindata,trainlable,testdata,testlabels):
    x = tf.placeholder("float",[None,32, 32, 3])  
    y_ = tf.placeholder("float",[None,10])
    keep_prob = tf.placeholder("float")
    W_conv1 = weight_variable([5,5,3,36])  
    b_conv1 = bias_variable([36])
      
    x_img = tf.reshape(x,[-1,32,32,3])  
    h_conv1 = tf.nn.relu(conv2d(x_img,W_conv1)+b_conv1)  
    h_pool1 = max_pool_2x2(h_conv1) 
    
    W_conv2 = weight_variable([5,5,36,72])
    b_conv2 = bias_variable([72])   
    h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)  
    h_pool2 = max_pool_2x2(h_conv2)  
    
    W_fc1 = weight_variable([8*8*72,1296])  
    b_fc1 = bias_variable([1296])  
    h_pool2_flat = tf.reshape(h_pool2,[-1,8*8*72])  
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1) + b_fc1)  
    
    h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)  
    W_fc2 = weight_variable([1296,10])  
    b_fc2 = bias_variable([10])  
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)  
    cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))  
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)  
    correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))  
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())  
    saver = tf.train.Saver()
    for i in range(1000):  
        if i % 10 == 0:  
            train_accuracy=accuracy.eval(feed_dict={x: testdata, y_: testlabels, keep_prob:1.0})
            print ("step %d, training accuracy %g" % (i, train_accuracy))
            saver.save(sess, "F:/test/test/model.ckpt")
        sj_data = []
        sj_lable = []
        for j in range(100):
            sj=random.randint(0, 1000)
            sj_data[j,:,:]=traindata[sj,:,:]
            sj_lable[j,:,:]=trainlable[sj,:,:]
        train_step.run(feed_dict={x: traindata, y_: trainlable, keep_prob:0.001})  
    

   
def load(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict["data"],dict["labels"]


def labels_vector(l):
    Labels = []
    m = len(l)
    for i in range(m):
        temp = zeros(10)
        temp[l[i]]=1
        Labels.append(temp)
    return Labels
def to1024(l):
    Labels = []
    m = len(l)
    for i in range(m):
        Labels.append(l[i:1024])
    return Labels
trainingMat,Labels=load('F:/cifar-10-batches-py/data_batch_1')
Labels=to_categorical(Labels)
trainingMat = dstack((trainingMat[:, :1024], trainingMat[:, 1024:2048],
                         trainingMat[:, 2048:])) / 255.
trainingMat = reshape(trainingMat, [-1, 32, 32, 3])

testTrainingMat,testLabels=load('F:/cifar-10-batches-py/test_batch')
testLabels=to_categorical(testLabels)
testTrainingMat = dstack((testTrainingMat[:, :1024], testTrainingMat[:, 1024:2048],
                         testTrainingMat[:, 2048:])) / 255.
testTrainingMat = reshape(testTrainingMat, [-1, 32, 32, 3])

creatCNN(trainingMat,Labels,testTrainingMat,testLabels)

#to_categorical

