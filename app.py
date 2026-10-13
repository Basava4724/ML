#import this
x = 1
print(id(x))
ch = 'A'
print(type(ch))
sentence = "my age is "
age = 19
print(sentence+str(age))
no = "15.9"
print(int(float(no)))
a,b,c,d,= 10,20,30,40 # valid
a=b=c=d= 10 #valid
# swappin of 2 numbers without temp
x= 10
y = 20
x,y= y,x
print(x,y)

# floor division //
x = 3
y = 2
print(x//y)
# Exponential Operator
print(x ** y)


print("S1" ,end="")

print("S2",end="")

print("S3")

# f-strings
x= 10
y = 20
print(f"the sum of {x} and {y} is {x+y}")

# bitwise operator
x = 10
y = 7
print(x & y)
# 8 4 2 1
#1 0 1  0   --10
# 0 1 1 1  --7
#0 0 1 0 --2   --ans 2 for 10 & 7

x = 10
y = 2
print(x << y)


x= 10
if x>0:
    print(x)
else:
    print("not found")
# short form of if
print("True block") if x>5 else print("False block")
# membership operator
name = "abcd"
if "abc" in name:
    print("present")
else:
    print("absent")
# i =0
# x = 10
# while i<=6:
#     x+=3
#     if x > 16:
#         x+=1
#         continue 
#     i += 1
# else:
#     print("ninja")


# for loop
for i in range(1,11,2): # 1= starting frp,m , 11 = ending , 2 = num of steps
    print(i)

for i in range(7,-1,-1):
    print(i)

# collections
# 1. list
# 2.tuple
# 3.set
# 4.dictionary

# lists
data = [10,20,30]
# add
data.append(60)
print(data)
data.insert(2,90) # insert
print(data)
# update 
data[-1] = 50
print(data)
# delete
data.pop() # removes from top
print(data)
data.pop(3) #  by index
data.remove(10) # by value
# reading
for v in data:
    print(v)

list1 = [10,20,30]
list2= [40,50]
print(list1 +list2) # concate
data.sort(reverse=True)



data = [n for n in range(1,21) if n%2==0]
print(data)
# create a list to have all not vowel from the name
name = "ababcdefghij"
data= [ch for ch in  name if ch not in 'aeiou']
print(data)

# tuple 

data = (1,2,3)

data = (3.14,)
print(type(data))

# set
data = {2,4,5,56,43}
print(data)

data.add(89)
data.remove(2)
for v in data:
    print(v)

# set operations
a = {1,2,3,4,5}
b = {4,5,6,7}
print(a.union(b))
print(a.difference(b))
 # dictionary
data ={
    "name" : "basava",
    "usn" : "133"
}
print(data)
# add
data['college'] = "SCEM" # adding new key value in dic
print(data)
# update 
print(data['name'])
# list of dictionary
data = [

    {"name": "basava"},
    {"age":"12"}
]
data = {
    "type": "ecommerce",
    "warehouse_data": [
        {"product": "A", "qty": 15},
        {"product": "B", "qty": 25},
        {"product": "C", "qty": 35}
    ]
}

total_qty = 0
for d in data['warehouse_data']:
    total_qty += d['qty']

print(total_qty)

data = {
    "type":"ecommerce",
    "warehouse_data":[
        {"category":"Smart Phones", "products":[
            {"product":"iphone","ratings":[4.5, 4.9]},
            {"product":"nothing","ratings":[3.9, 4.2]},
            {"product":"galaxy","ratings":[3.8, 4.6]}
        ]},
        {"category":"Laptops", "products":[
                    {"product":"MacBook","ratings":[4.2, 4.6]},
                    {"product":"HP","ratings":[3.6, 4.4]},
                ]}
    ]
}
# functions
def returnMultipleValues():
    x = 10.5
    y = 10
    z = 'A'
    return x,y,z
print(returnMultipleValues()) # tuple 

# Arbitrary Function

def arb(*args):
    print(args)      # tuple
arb(10,20,30,40)

# k args
def kargs(**args):
    print(args) # dictionary
kargs(name = "A",age = 19)

# lambda function
area_of_circle = lambda pie,r:pie*(r**2)

print(f"area of the of circle :{area_of_circle(3.14,10)}")

# exception handling
x = 10
y = 0
try:
    z = x/y
    print(z)
except Exception as e:
    print("division by zero {e}")
print("After Exception")
