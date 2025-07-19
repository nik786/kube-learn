
```

pip install -q gdown

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline



df = pd.read_csv("insurance_data.csv")
df.head()

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.age.to_frame(),df.bought_insurance,train_size=0.8)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


model.fit(X_train, y_train)


# make predictions
y_predicted = model.predict(X_test)
y_predicted

model.predict_proba(X_test)

model.score(X_test,y_test)

## Building the Logistic regression model by hand

import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


age = 35
prediction_function(age)

threshold = 0.5


age = 35
print("Will buy insurance:", prediction_function(age) > threshold)


age = 45
print("Will buy insurance:", prediction_function(age) > threshold)





















```
