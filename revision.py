# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:59:33 2023

@author: Thibaut R
"""
import numpy as np
import matplotlib.pyplot as plt
course = {}
mean=0;
course= ({1:"Fast Money As",2:21.0},
         {1:"Only Muscles Steel",2:6.2},
         {1:"Onmyway Fortuna",2:3.4},
         {1:"Opal Stone",2:9.6})
for i in range(0,len(course)-1):
    mean=mean+course[i][2]
mean=(mean/len(course))
print(mean)
print("The average of betting is {}".format(int(mean)))

x=np.linspace(0,10,100)
y=x+1
x=plt.xlim(0,8)
y=plt.ylim(1,7)
plt.plot(x,y)
plt.legend()
plt.show()

mat=np.array([[1,2,3],[3,4,5],[5,6,7]])
mat2=np.array([[1,2,3],[3,4,5],[5,6,7]])
mat3=mat@mat2
print(mat3)
print(mat.T)
print(np.zeros((3,4)))

try : 
   int(input("zizi"))
except :
    print("pas un chiffre connard")


    

    