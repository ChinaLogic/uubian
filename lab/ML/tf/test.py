from numpy import *
import operator
from os import listdir
import tensorflow as tf

def img2vector(filename):
    returnVect = zeros((1,784))
    fr = open(filename)
    for i in range(28):
        lineStr = fr.readline()
        for j in range(28):
            returnVect[0,28*i+j] = int(lineStr[j])
    return returnVect

Labels = []
trainingFileList = listdir('traindata')
m = len(trainingFileList)
trainingMat = zeros((m,784))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     
    classNumStr = int(fileStr.split('_')[0])
    temp = zeros(10)
    temp[classNumStr]=1
    Labels.append(temp)
    trainingMat[i,:] = img2vector('traindata/%s' % fileNameStr)
testLabels = []
testTrainingFileList = listdir('testdata')
testm = len(testTrainingFileList)
testTrainingMat = zeros((testm,784))
for i in range(testm):
    fileNameStr = testTrainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     
    classNumStr = int(fileStr.split('_')[0])
    temp = zeros(10)
    temp[classNumStr]=1
    testLabels.append(temp)
    testTrainingMat[i,:] = img2vector('testdata/%s' % fileNameStr)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.InteractiveSession()
sess.run(init)
for i in range(10):
    sess.run(train_step, feed_dict={x: trainingMat, y_: Labels})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval({x: testTrainingMat, y_: testLabels}))
















