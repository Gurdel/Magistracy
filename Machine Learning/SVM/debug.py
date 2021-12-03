import numpy as np
import pandas as pd
from random import seed
from random import randrange
from math import exp
from math import floor

#split data into train and test
def cross_val_split(data_X,data_Y,test_size,seed_val):
	data_x = data_X.tolist()
	data_y = data_Y.tolist()
	seed(seed_val)
	train_size = floor((1 - test_size)*len(data_x))
	train_x = []
	train_y = []
	while(len(train_x)<train_size):
		index = randrange(len(data_x))
		train_x.append(data_x.pop(index))
		train_y.append(data_y.pop(index))
	return train_x,train_y,data_x,data_y

#columnwise max-min statistics for scaling
def statistics(x):
	cols = list(zip(*x))
	stats = []
	for e in cols:
		stats.append(np.array([min(e),max(e)]))
	return stats

#scale the features
def scale(x, stat):
	for row in x:
		for i in range(len(row)):
			row[i] = (row[i] - stat[i][0])/(stat[i][1] - stat[i][0])


#convert different classes into different columns to implement one v/s all
def one_vs_all_cols(s):
	res = []
	m = list(set(s))
	m.sort()
	for i in range(len(s)):
		new = [0]*len(m)
		new[m.index(s[i])] = 1
		res.append(new)
	return m, np.array(res)

#Theta transpose x Feature Vector
def ThetaTX(Q,X):
    det = 0.0
    sum = np.sum(np.array(Q) * np.array(X))
    for i in range(len(Q)):
        det += X[i]*Q[i]
    return det

def sigmoid(z):
	return 1.0/(1.0 + exp(-z))

#Gradient Descent on the weights/parameters
def gradDescent(theta, c, x, y, learning_rate):
	oldTheta = theta[c]
	for Q in range(len(theta[c])):
		derivative_sum = 0 
		for i in range(len(x)):
			derivative_sum += (sigmoid(ThetaTX(oldTheta, x[i])) - y[i])*x[i][Q]
		theta[c][Q] -= learning_rate*derivative_sum

#predictions using trained weights
def predict(data, theta):
	predictions = []
	for row in data:
		hypothesis = []
		multiclass_ans = [0]*len(theta)
		for c in range(len(theta)):
			z = ThetaTX(row,theta[c])
			hypothesis.append(sigmoid(z))
		index = hypothesis.index(max(hypothesis))
		multiclass_ans[index] = 1
		predictions.append(multiclass_ans)
	return predictions

def accuracy(predicted, actual):
	n = len(predicted)
	correct = 0
	for i in range(n):
		if(predicted[i]==actual[i]):
			correct+=1
	return correct/n

def cross_validation(x, y, x_res, y_res, test_data_size, validations, learning_rate, epoch):
	print("Epochs count: ",epoch)
	accuracies = []
	for valid in range(validations):
		x_train, y_train, x_val, y_val = cross_val_split(x,y,
                                                     test_data_size,valid+1)
		#converting y_train to classwise columns with 0/1 values
		classes = []
		for i in range(len(label_map)):
			classes.append([row[i] for row in y_train])
		#Initialising Theta (Weights)
		theta = [[0]*len(x_train[0]) for _ in range(len(classes))]
		#training model
		for i in range(epoch):
			print('.', end='')
			for class_type in range(len(classes)):
				print(',', end='')
				gradDescent(theta,class_type,x_train,classes[class_type],learning_rate)
		#Predicting using validation data
		y_pred = predict(x_val, theta)
		#Calculating accuracy
		accuracies.append(accuracy(y_pred,y_val))
		print("Validation", valid+1, "accuracy: ", accuracies[valid])
		y_pred = predict(x_res, theta)
		print("Test data accuracy: ", accuracy(y_pred,y_res))
	
	return sum(accuracies)/len(accuracies), y_pred


dataset = pd.read_csv("data.csv")
data = dataset.values

X = data[:, 2:5]
y = data[:, 1]

print(y[:10], X[:2])
import numpy as np
a = np.array([8, 9, 7])
stats = statistics(X)
scale(X,stats)
label_map, y = one_vs_all_cols(y)
y = np.array(y)
print(label_map)
print(y[:2], X[:2])

#Splitting dataset into training and testing data
test_data_size = 0.2
learning_rate = 0.02
epoch = 50
validations = 5

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                          test_size=0.2, random_state=42)
final_score,y_pred = cross_validation(X_train,y_train,X_test,y_test,test_data_size,validations,
                                      learning_rate,epoch)