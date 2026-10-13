import numpy as np
#numpy array
# 0 dimension arry
zd_array=np.array(50)
print(zd_array)
print(f"zero Dimension : {zd_array.ndim}") 


# 1D Array
data=[10,20,30,40,50]
one_d_array=np.array(data)
print(one_d_array)
print(f"One D Array Dimension :{one_d_array.ndim}")
print(f"Shape of the array : {one_d_array.shape}")
print(f"Size of the array :{one_d_array.size}")
print("==========================================================================================================================")


# 2D Array
data=[
    [10,20,30,40],
    [40,50,60,70]
]
two_d_array=np.array(data)
print("2 D Array")
print(f"two D Array Dimension :{two_d_array.ndim}")
print(f"Shape of the array : {two_d_array.shape}")
print(f"Size of the array :{two_d_array.size}")
print("==========================================================================================================================")


#3D Array
data=[[[10,20,30],
       [40,50,60]
],
[[50,60,70],
 [80,90,100]
 ],
[
[30,40,60],
[50,60,70]
]]

three_d_array=np.array(data)
print(f"Three D Array Dimension :{three_d_array.ndim}")
print(f"Shape of the array : {three_d_array.shape}")
print(f"Size of the array :{three_d_array.size}")

print("==========================================================================================================================")


#Reshaping of the Array
data=[
    [10,20,30,40],
    [40,50,60,70]
]
two_d_array=np.array(data)
print(two_d_array.reshape(4,2))


print("==========================================================================================================================")

#Pandas
import pandas as pd
df=pd.read_csv("dataset_2.csv")
print(df)
print("==========================================================================================================================")
print(df.head())
print("==========================================================================================================================")

print(df.tail())
print("==========================================================================================================================")



#Specific coloumn
print(df[['Area_SqFt','Rooms','Price']])
print("==========================================================================================================================")


#describe

print(df.describe())
print("==========================================================================================================================")


#Location
print(df.groupby('Location')['Location'].count())
print("==========================================================================================================================")
#street type
print(df.groupby('Street_Type')['Street_Type'].count())
print("==========================================================================================================================")

# furnishing
print(df.groupby('Furnishing')['Furnishing'].count())
print("==========================================================================================================================")


# Property_Type

print(df.groupby('Property_Type')['Property_Type'].count())
print("==========================================================================================================================")


print(df.groupby('Property_Type')['Area_SqFt'].mean())

print("==========================================================================================================================")

print(df.groupby('Property_Type')[['Area_SqFt','Rooms','Build_Year']].mean())
print("==========================================================================================================================")

print(df.groupby('Location')[['Area_SqFt','Rooms','Build_Year']].mean())

print("==========================================================================================================================")

# Check How many Null Values are There
print(df.isna().sum())
print("==========================================================================================================================")

#Remove the Null Values
df.dropna(inplace=True)
print(df)
print("==========================================================================================================================")
print(df.isna().sum())
print("==========================================================================================================================")


# drop Duplicates

df.drop_duplicates(inplace=True)
print(df)


# import matplotlib.pyplot as plt
# df.plot(kind='scatter',x='Area_SqFt',y='Price')
# plt.show()

#Factorization
'''
df_copy=df.copy()
df['original_labels_location']=df_copy['Location']
df['original_labels_Street_type']=df_copy['Street_Type']
df['original_labels_furnishing']=df_copy['Furnishing']
df['original_labels_Property_type']=df_copy['Property_Type']
df['original_labels_has_pool']=df_copy['Has_Pool']
'''

df['Location']=pd.factorize(df['Location'])[0]
df['Street_Type']=pd.factorize(df['Street_Type'])[0]
df['Furnishing']=pd.factorize(df['Furnishing'])[0]
df['Property_Type']=pd.factorize(df['Property_Type'])[0]
df['Has_Pool']=pd.factorize(df['Has_Pool'])[0]
'''
# Numberic Lables For Location
print(df.groupby(['original_labels_location','Location'])['Location'].count())
print(df.groupby(['original_labels_Street_type','Street_Type'])['Street_Type'].count())
print(df.groupby(['original_labels_furnishing','Furnishing'])['Furnishing'].count())
print(df.groupby(['original_labels_Property_type','Property_Type'])['Property_Type'].count())
print(df.groupby(['original_labels_has_pool','Has_Pool'])['Has_Pool'].count())


'''
print(df)

from sklearn.linear_model import LinearRegression

# Independent Variables

X=df[['Area_SqFt','Rooms','Build_Year','Location','Street_Type','Furnishing','Property_Type','Has_Pool']]

# Dependent Variable / Target Variable

y=df['Price']

# Train the data into the Model
model=LinearRegression()
model.fit(X,y)
# Test Data
Area_SqFt=2200
Rooms=3
Build_Year=2024
Location=0  #jaipur
Street_Type=2 #HighWay FAcing
Furnishing=0  # Furnished
Property_Type=0  #Apartment
Has_Pool=0 #no

test_data=[[Area_SqFt,Rooms,Build_Year,Location,Street_Type,Furnishing,Property_Type,Has_Pool]]

result=model.predict(test_data)
print(result)