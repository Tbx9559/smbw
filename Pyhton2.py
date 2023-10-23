# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

    
elec=int(input("Enter unit"))
bill=0
if elec < 100:
    print("Price 0")
if elec>=100 and elec <200:
    print("Price : {}".format((elec-100)*5))
if elec>=200:
    print("Price: {}".format(100*5+(elec-200)*10))
    



for i in range(4):
    for j in range(3):
        print("i={}, j={}".format(i,j))
sum=0
fin=int(input("Enter number"))
for i in range(fin+1):
    sum=sum+i
print(sum)

b=True
num=int(input("Enter number"))
for i in range (2,(num//2)+1):
    if num%i==0:
        b =False
if b==False:
    print("{} n'est pas premier".format(num))
else:
    print("{} est premier".format(num))
    
stop=True        
name=[]
note=[]
while stop==True:
    na=(input("Enter a name or tap enter to finish : "))
    name.append(na)
    if na=="":
        break
    no=int(input("Enter a number : "))
    note.append(no)


sum=0
for i in range (0,len(name)-1):
    sum=sum+note[i]
    print("{}  {}".format(name[i],note[i]))
print("The average is {}".format(sum/(len(name)-1)))   

sum=0
c=0
mean=0

liste = []
value ="value"
while value !=""  :
    value=input("Enter number or tape enter to exit")
    liste.append(value)
    if value!="" :
        sum=sum+int(value)
        c=c+1
        mean=sum/c
        
print("the mean is : {}".format(mean))

Dict={}
Dict=({1: 'Geeks',2:'For',3:'Greeks'},
      {1: 'Seven',2:'Five',3:'Seven'})

print(Dict[1][1])

Element={}
Element=({1: 'H',2:'Hydrogen'  ,3:'1' ,4:14  ,5:20},
         {1: 'HE',2:'Helium'   ,3:'2' ,4:1   ,5:4},
         {1: 'LI',2:'Lithium'  ,3:'3' ,4:453 ,5:1603},
         {1: 'BE',2:'Beryllium',3:'4' ,4:1560,5:2742},
         {1: 'B',2:'Boron'     ,3:'5' ,4:2349,5:4200},
         {1: 'C',2:'Carbon'    ,3:'6' ,4:3915,5:3915},
         {1: 'N',2:'Nitrogen'  ,3:'7' ,4:63  ,5:77},
         {1: 'O',2:'Oxygen'    ,3:'8' ,4:54  ,5:90},
         {1: 'F',2:'Fluorine'  ,3:'9' ,4:53  ,5:85},
         {1: 'NE',2:'Neon'     ,3:'10',4:25  ,5:27}
         )
print ("Hello user, choose your element")
name=(input("Use the symbol").upper())
temp=int(input("Choose now the temperature in K"))
for i in range (0,len(Element)-1):
    if Element[i][1]==name:
        break
if name=='NE':
    i=i+1
print(i)
print(Element[i][2])
if temp >= Element[i][5]:
    print(("The element is gas at the point {}K").format(temp))
elif temp >=Element[i][4]:
    print(("The element is liquid at the point {}K").format(temp))
else:
    print(("The element is solid at the point {}K").format(temp))
    
import numpy as np
vector=np.linspace(10,30,21)
print(vector)


import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(x,y)
plt.title("Graph of x^2 vs x")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,3*np.pi,500)
plt.plot(x, np.sin(x**2))
plt.title("A simple chirp")


x=np.linspace(-2,2,101)
y=x**2
plt.plot(x)
plt.show()


x=np.linspace(-2,2,101)
y=x**2
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.title("Chart Title")
plt.plot(x,y)
plt.show()



x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y, label="x2")
y2=x**4
plt.plot(x,y2, label="x4")
plt.legend()
plt.show()


a=int(input("Enter an integer value"))
x=np.linspace(-1,1,a)
y=np.cos(2*np.pi*x)
plt.title("Body function cos(2pix)")
plt.xlim(-1,1)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.savefig("cos2pix.png")
plt.show()

number=int(input("enter number of value"))
x=np.linspace(2,10,number)
temp=float("enter temp in k")
p=(0.08206*temp)/x
plt.xlabel("x")
plt.ylabel("y")
plt.title("my graph")
plt.savefig("isotherm.jpg")
plt.plot(x,p)
plt.show()

n=int(input("number of values"))
min=int(input("min"))
max=int(input("max"))
x0=float(input("xo"))
s=float(input("s"))
x=np.linspace(min,max,n)
y=np.exp(-0.5*(((x-x0)**2)/s**2))/(2*np.pi)**0.5
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian")
plt.savefig("isotherm.jpg")
plt.plot(x,p)
plt.show()




Ang_to_nano= np.linspace(1,5,21)
print(Ang_to_nano)
le = len(Ang_to_nano)
for i in range(le):
        Ang_to_nano[i] = Ang_to_nano[i]/10   
print(Ang_to_nano)        

import math

def ex2():
    x0 = float(input("Enter the value of X0 : "))
    s = float(input("Enter the value of s : "))
    n1 = float(input("Enter the minimal value of the interval : "))
    n2 = float(input("Enter the maximal value of the interval : "))
    n3 = int(input("Enter the the number of points : "))
    x = np.linspace(n1, n2, n3)
    y = np.zeros(n3)
    for i in range(n3):
        y[i] = math.exp((-(x[i]-x0)**2)/(2 * s**2))/math.sqrt(2*math.pi)
    for i in range(n3):
        print(f"{x[i]:.3f} {y[i]:.5f}")


    


def ex3():

    temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4,
                20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    temp_mar = np.asarray(temp_mar)
    mean = temp_mar.mean()
    print(f"The average sea surface temperature in 2014 is {mean:2f} ")
    mini = temp_mar.min()
    maxi = temp_mar.max()
    for i in range(len(temp_mar)):
        if mini == temp_mar[i]:
            moismin = months[i]
            
    for i in range(len(temp_mar)):
        if maxi == temp_mar[i]:
            moismax = months[i]
    print(f"The month in which the sea surface has been coldest is {moismin} with {mini} degrees")
    print(f"The month in which the sea surface has been warmest is {moismax} with {maxi} degrees")
    


def ex4():
    nbstudent=int(input("Enter the number of students : "))
    mat=np.zeros((nbstudent,4))
    for i in range (nbstudent):
        theorie=int(input(f"Enter the theory note of the student number {i} : "))
        problem=int(input(f"Enter the problem note of the student number {i} : "))
        totalmark=0.4*theorie+0.6*problem
        mat[i,0]=int(i)
        mat[i,1]=theorie
        mat[i,2]=problem
        mat[i,3]=totalmark
    print()
    print("st.nbr theorie problem finalmark")
    print(mat)
    
    print()
    maxi=0
    mini=20
    index=0
    sum=0
    for i in range (nbstudent):
        sum+=mat[i,3]
        if(maxi<mat[i,3]):
            maxi=mat[i,3]
            index=int(mat[i,0])
        if(mini>mat[i,3]):
            mini=mat[i,3]
    print(f"maximum total grade : {maxi} and the student number {index} obtained it")
    print(f"minimum total grade : {mini}")
    avg=sum/nbstudent
    print(f"the average is {avg}")












    

    
    

        

    
    
    
    
