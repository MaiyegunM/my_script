"""author: Maiyegun Muisi"""


#This is a code that calculates the area of a circle
print("Calculate the area of a circle")


radius = float(input("Please enter the radius of a circle: "))
area =3.14*radius*radius
print("area of cirlcle is: ",area)
 

#This is a program that calculates the area of a triangle
print("Calculate the area of a triangle")
a = int(input("Please input the length first side: "))
b = int(input("please input the length second side: "))
c = int(input("please input the length third side: "))

p = (a+b+c)
s = p/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of a triangle is = ",area)
print("perimeter of a triangle is = ",p)
print("semi perimter of a triangle is = ",s)


#This is a program to calculate simple interest
print("calculate simple interest")

p=int(input("please enter your principal amount= "))
r=float(input("please enter your rate of interest= "))
t=float(input("please enter time= "))
si=(p*r*t)/100
print("The simple interest= ",si)


