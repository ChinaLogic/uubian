import tensorflow as tf  
from os import listdir
from numpy import *
  
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
    x = tf.placeholder("float",[None,784])  
    y_ = tf.placeholder("float",[None,10])
    keep_prob = tf.placeholder("float")
    W_conv1 = weight_variable([5,5,1,32])  
    b_conv1 = bias_variable([32])  
    x_img = tf.reshape(x,[-1,28,28,1])  
    h_conv1 = tf.nn.relu(conv2d(x_img,W_conv1)+b_conv1)  
    h_pool1 = max_pool_2x2(h_conv1) 
    W_conv2 = weight_variable([5,5,32,64])
    b_conv2 = bias_variable([64])   
    h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)  
    h_pool2 = max_pool_2x2(h_conv2)  
    W_fc1 = weight_variable([7*7*64,1024])  
    b_fc1 = bias_variable([1024])  
    h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])  
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1) + b_fc1)  
    h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)  
    W_fc2 = weight_variable([1024,10])  
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
            saver.save(sess, "D:/test/test/model.ckpt")
        sj_data = zeros((100,784))
        sj_lable = zeros((100,10))
        for j in range(100):
            sj=random.randint(0, 50000)
            sj_data[j,:]=traindata[sj,:]
            sj_lable[j,:]=trainlable[sj,:]
        train_step.run(feed_dict={x: sj_data, y_: sj_lable, keep_prob:0.5})  
    

def img2vector(filename):
    returnVect = zeros((1,784))
    fr = open(filename)
    for i in range(28):
        lineStr = fr.readline()
        for j in range(28):
            returnVect[0,28*i+j] = int(lineStr[j])
    return returnVect

trainingFileList = listdir('D:/traindata')
m = len(trainingFileList)
trainingMat = zeros((m,784))
Labels = zeros((m,10))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     
    classNumStr = int(fileStr.split('_')[0])
    temp = zeros((1,10))
    temp[0,classNumStr]=1
    Labels[i,:]=temp
    trainingMat[i,:] = img2vector('D:/traindata/%s' % fileNameStr)
testLabels = []
testTrainingFileList = listdir('D:/testdata')
testm = len(testTrainingFileList)
testTrainingMat = zeros((testm,784))
for i in range(testm):
    fileNameStr = testTrainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     
    classNumStr = int(fileStr.split('_')[0])
    temp = zeros(10)
    temp[classNumStr]=1
    testLabels.append(temp)
    testTrainingMat[i,:] = img2vector('D:/testdata/%s' % fileNameStr)    

creatCNN(trainingMat,Labels,testTrainingMat,testLabels)









