import numpy as np
import pandas as pd

dataset=pd.read_csv('Churn_Modelling.csv')

X=dataset.iloc[:,3:13].values
y=dataset.iloc[:,13].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()

cat_feats=[1,2]

for i in cat_feats:
    X[:,i]=le.fit_transform(X[:,i])

ohe=OneHotEncoder(categorical_features=[1])

X=ohe.fit_transform(X).toarray()
X=X[:,1:]

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X=ss.fit_transform(X)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)


# conda install -c conda-forge keras

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()

classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=11))
classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))
classifier.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
classifier.fit(xtrain,ytrain,batch_size=10,epochs=100)
ypred=classifier.predict(xtest)
ypred=(ypred>0.5)

from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(ytest,ypred)
