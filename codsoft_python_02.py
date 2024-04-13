#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Select operation-\n"\
     "1. Addition\n"\
     "2. Subtraction\n"\
     "3. Multiplication\n"\
     "4. Divison\n")

select= int(input("select operation from 1,2,3,4:"))
number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))
if select==1:
    print("ans:",number_1,"+",number_2,"=",add(number_1,number_2))
elif select==2:
    print("ans:",number_1,"-",number_2,"=",subtract(number_1,number_2))
elif select==3:
    print("ans:",number_1,"*",number_2,"=",multiply(number_1,number_2))
elif select==4:
    print("ans:",number_1,"/",number_2,"=",divide(number_1,number_2))
else:
    print("invalid input")    


# In[ ]:




