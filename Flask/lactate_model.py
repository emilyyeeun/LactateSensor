#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


# ### Reading in CSV file

# In[2]:


patients = pd.read_csv('./patients.csv')


# ### Creating Model

# In[3]:


test = patients[patients.Glucose <= (7.6*18)]
test = test[test.Glucose > (7.0*18)]
test1 = test[test.Lactate <= 1.7]
test2 = test[test.Lactate > 2.3]
patients.drop(test1.index, inplace=True)
patients.drop(test2.index, inplace=True)


# In[4]:


test = patients[patients.Glucose <= (8.2*18)]
test = test[test.Glucose > (7.6*18)]
test1 = test[test.Lactate <= 1.3]
test2 = test[test.Lactate > 1.7]
patients.drop(test1.index, inplace=True)
patients.drop(test2.index, inplace=True)


# In[5]:


test = patients[patients.Glucose <= (9.0*18)]
test = test[test.Glucose > (8.2*18)]
test1 = test[test.Lactate <= 1]
test2 = test[test.Lactate > 1.3]
patients.drop(test1.index, inplace=True)
patients.drop(test2.index, inplace=True)


# In[6]:


test = patients[patients.Glucose > (9.0*18)]
test1 = test[test.Lactate > 1]
patients.drop(test1.index, inplace=True)


# In[7]:


test = patients[patients.Glucose <= (7.0*18)]
test1 = test[test.Lactate <= 2.3]
patients.drop(test1.index, inplace=True)


# In[8]:


encode = lambda x: 1 if x <= (7.0*18) else 0
patients['G_Range1'] = patients['Glucose'].map(encode)


# In[9]:


encode = lambda x: 1 if x <= (7.6*18) else (1 if x > (7.0*18) else 0)
patients['G_Range2'] = patients['Glucose'].map(encode)


# In[10]:


encode = lambda x: 1 if x <= (8.2*18) else (1 if x > (7.6*18) else 0)
patients['G_Range3'] = patients['Glucose'].map(encode)


# In[11]:


encode = lambda x: 1 if x <= (9.0*18) else (1 if x > (8.2*18) else 0)
patients['G_Range4'] = patients['Glucose'].map(encode)


# In[12]:


encode = lambda x: 1 if x > (9.0*18) else 0
patients['G_Range5'] = patients['Glucose'].map(encode)


# In[13]:


encode = lambda x: 1 if x<=1.0 else (2 if (x<=1.3 and x>1.0) else (3 if (x>1.3 and x<=1.7) else (4 if (x>1.7 and x<=2.3) else 5)))


# In[14]:


patients['Lactate_Ranges'] = patients['Lactate'].map(encode)


# In[15]:


y = patients['Lactate_Ranges']
X = patients[['Age', 'Male', 'Height', 'Weight','SpO2', 'HeartRate','G_Range1','G_Range2','G_Range3','G_Range4','G_Range5']]
train_end = int(np.floor(0.91*len(X)))
X_train = X[:train_end]
X_test = X[train_end:]
y_train_copy = y[:train_end]
y_test_copy = y[train_end:]
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
logregr = LogisticRegression().fit(X_train, y_train_copy)
pred1 = logregr.predict(X_test)
print(classification_report(y_test_copy, pred1))
print("MSE:", mean_squared_error(y_test_copy, pred1))
print("R^2:", r2_score(y_test_copy, pred1))

num_misclassified = sum(abs(y_test_copy - pred1))
print("Number classified wrong: ", num_misclassified)
print("Percentage classified wrong: ", num_misclassified/len(pred1))

plt.plot(range(len(y_test_copy)),y_test_copy)
plt.plot(range(len(y_test_copy)),pred1)
plt.legend(labels = ('Actual', 'Prediced'))


# ### Function to Predict Lactate Level

# In[16]:


def predict_lactate(gender, age, height, weight, spO2, heartrate, glucose):
    male = 1
    grange1 = grange2 = grange3 = grange4 = grange5 = 0
    if gender.lower() == 'female':
        male = 0
    if glucose/18 <= 7:
        grange1 = 1
    elif glucose/18 <= 7.6:
        grange2 = 1
    elif glucose/18 <= 8.2:
        grange3 = 1
    elif glucose/18 <= 9:
        grange4 = 1
    else:
        grange5 = 1
    pred = logregr.predict([[grange1, grange2, grange3, grange4, grange5, age, male, height, weight, spO2, heartrate]])
    if pred == 1:
        return '<= 1.0'
    elif pred == 2: 
        return '1.0 - 1.3'
    elif pred == 3:
        return '1.3 - 1.7'
    elif pred == 4:
        return '1.7 - 2.3'
    else:
        return '> 2.3'


# In[17]:


predict_lactate('Female', 22, 65, 123.5, 97, 80, 90)

