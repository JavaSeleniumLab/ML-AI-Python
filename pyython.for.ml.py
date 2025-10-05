import numpy as np
import pandas as p
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt


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
