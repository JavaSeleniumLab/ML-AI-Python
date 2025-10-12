import numpy as np 
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Creating arrays
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(arr)
print(arr.shape)
arr2 = arr.reshape(3,5)
print(arr2)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.ndim)
print(a)

#Arithmetic operations
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
result = np.add(a,b)
print(result)

print("===================================")
result = np.subtract(a,b)
print(result)

print("===================================")
result = np.multiply(a,b) #Element-wise multiplication
print(result)

print("===================================")
result = np.dot(a,b) #Matrix multiplication
print(result)       

print("===================================")
result = np.divide(a,b) #Element-wise division
print(result)   
print("===================================")

result = np.sqrt(a) #Square root
print(result)   
print("===================================")

print(np.mean(a)) #Mean
print(np.median(a)) #Median
print(np.std(a)) #Standard Deviation - difference from mean and deviation
print(np.var(a)) #Variance 
print("===================================")

#print(stats.mode(a)) #Mode - most frequently occuring value
print("===================================")


x = np.array(["Hello","World"])
y = np.array(["Hello","Everyone"])
print(np.concatenate((x,y))) #Concatenate arrays    
print("===================================")

string = "Hello, World!"
print(string.split(",")) #Split string into list    
print("===================================")

print(np.char.upper(string)) #Range of numbers with step size
print("===================================")
print(np.char.lower(string)) #Convert string to lowercase
print("===================================") 
print(np.char.replace(string, "World", "Everyone")) #Replace substring 
print("===================================")  

# OCTOBER 5TH -2025: 2 DIMENSIONAL ARRAYS
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
print(arr_2d.shape) #Shape of the array
print(arr_2d.ndim) #Number of dimensions    

# Accessing elements
print(arr_2d[0,0]) #First row, first column 
print("===================================")
# 3 dimensional array
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr_3d)
print("===================================")
arr_3d[1,1,1] = 99 #Modify element
print(arr_3d)
print("===================================")
#Slicing arrays 
print(arr_2d[0:2,1:3]) #First two rows, second and third columns
print("===================================")

#Iterating through arrays
for i in range(arr_2d.shape[0]): #Iterate through rows
    for j in range(arr_2d.shape[1]): #Iterate through columns
        print(arr_2d[i,j], end=" ")
    print() #New line after each row

print("===================================")
# Pandas DataFrames
data = {"A": [1,2,3,4,5], "B": [5,4,3,2,1], "C": ['a','b','c','d','e']}
ser_ies = pd.Series([10,20,30,40,50])
print(ser_ies)
df = pd.DataFrame(data)
print(df)
print("===================================")
print(ser_ies.head(2)) #First two rows
print("===================================")
print(df.tail(2)) #Last two rows
print("===================================")
print(df.describe()) #Statistical summary
print("===================================")
print(df.info()) #DataFrame info
print("===================================")
print(ser_ies.unique()) #Unique values in Series
print("===================================")    

ser_ies.apply(lambda x: x*2) #Apply function to each element
print(ser_ies.apply(lambda x: x**2))

print("===================================")
#Filtering data 
print(ser_ies[ser_ies > 25]) #Values greater than 25
print("===================================")
print(ser_ies[ser_ies % 20 == 0]) #Values divisible by 20
print("===================================")
print(ser_ies[ser_ies > 25][ser_ies < 45]) #Values between 25 and 45
print("===================================")
data = {"A": [1,2,3,4,5], "B": [5,4,3,2,1], "C": ['a','b','c','d','e']}
print(pd.DataFrame(data))
print("===================================")
data2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
df2 = pd.DataFrame(data2)
print(df2)
print("===================================")
df.columns = ['X','Y','Z'] #Rename columns
print(df)
print("===================================")
df.columns = ['X','Y','Z'] #Rename columns
df2.index = ['Row1','Row2','Row3'] #Rename index
print(df2)      
print("===================================")
df.iloc[0,0] = 99 #Modify element by position
print(df)
print("===================================")
df.loc[1,'Y'] = 88 #Modify element by label
print(df)
print("===================================")

categories = ['High','Medium', 'Low']
values = ['low', 'High','Medium','low', 'High', 'Low', 'High', 'High','High']

cat_var= pd.Categorical(values, categories, ordered=True)
print(cat_var)


data = {'A' : [1,2,3,4,5], 'B':[5,4,3,2,1]}
df = pd.DataFrame(data)
print(df)
print("===================================")    
df.plot()
plt.show()
print("===================================")
df.plot(kind='bar')
plt.show()  
print("===================================")