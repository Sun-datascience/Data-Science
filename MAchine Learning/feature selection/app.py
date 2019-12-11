from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=datasets.load_boston()
x=data.data
y=data.target

x=pd.DataFrame(x)
#print(x)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)

model=LinearRegression()
model.fit(xtrain,ytrain)
print('accuracy score {}'.format(model.score(xtest,ytest)*100))
preds=model.predict(xtest)
print('error {}'.format(mean_squared_error(ytest,preds)))

weights=list(zip(x.columns,model.coef_))


def secondelem(elem):
    return elem[1]
weights.sort(key=secondelem,reverse=True)
print(weights)


newfeatures=[weights[i][0] for i in range(0,5)]
print(newfeatures)

model.fit(xtrain[newfeatures],ytrain)
print('accuracy score {}'.format(model.score(xtest[newfeatures],ytest)*100))
preds=model.predict(xtest[newfeatures])
print('error {}'.format(mean_squared_error(ytest,preds)))


newfeatures=[weights[i][0] for i in range(len(weights)) if weights[i][1]>0]
print(newfeatures)

model.fit(xtrain[newfeatures],ytrain)
print('accuracy score {}'.format(model.score(xtest[newfeatures],ytest)*100))
preds=model.predict(xtest[newfeatures])
print('error {}'.format(mean_squared_error(ytest,preds)))


for i in range(0,len(newfeatures)):
    newfeatures1 = list()
    for j in range(0,i+1):

        newfeatures1.append(newfeatures[j])
    print(newfeatures1)
    model.fit(xtrain[newfeatures1],ytrain)
    print('accuracy score {}'.format(model.score(xtest[newfeatures1],ytest)*100))
    preds=model.predict(xtest[newfeatures1])
    print('error {}'.format(mean_squared_error(ytest,preds)))


