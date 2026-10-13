import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
df=pd.read_csv("logistic_data.csv")
#print(df.head(10))
print(df.groupby('Pass')['Pass'].count())
# prepare the independent variable X
X =  df[['Hours_Studied','Attendance']]
y = df['Pass']

# split the data into training set and test set
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=42)

# logistic regression model
model  = LogisticRegression()
# training process
model.fit(X_train,y_train)
print(X_test)
result = model.predict(X_test)
print(result)

# accuracy score
print(f"Accuracy Score :{accuracy_score(y_test,result)}")

# classification 
print(classification_report(y_test,result))