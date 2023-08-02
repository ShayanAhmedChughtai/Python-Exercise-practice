#ex 1
# print("Twinkle, twinkle, little star \n\tHow I wonder what you are! \n\t\tUp above the world so high \n\t\tLike a diamond in the sky. Twinkle, twinkle, little star \n\tHow I wonder what you are")

#ex 2

# import sys
# print("Python version")
# print(sys.version)
# print("system version")
# print(sys.version_info)

#ex 3
# 
# fname=input("Enter your first name : ")
# lname=input("Enter your last name : ")
# print(lname,fname)

#ex 4
# 
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print("The area of the circle with radius is" + str(int(r)) +" is :"+ str(pi*r**2))
#           
#ex 5

# colour_list=["red","blue","green","black"]
# print(colour_list[0],colour_list[-1])

# ex 6
# 
# import datetime
# now=datetime.datetime.now()
# print("Current date ")
# print(now.strftime("%m-%d-%Y "))

# list=[]
# for i in range(1,51):
#     list.append(i)
# print(list)    
 
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)



# num=int(input("Enter a integer"))
# num2=num*11
# num3=num*111
# result=(num+num2+num3)
# print(result)
# 
# 
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# print(dict



# tup1=(9,2,7,3,5,)
# print(tup1)
# list=list(tup1)
# list.sort()
# tup1=tuple(list)

# print(tup1)


# a=int(input("Enter number:"))
# b=int(input("Enter number:"))
# c=int(input("Enter number:"))
# 
# 
# 
# if a>b and a>c:
#     print(a ,"is greater")
# elif b>a and b>c:
#     print(b,"is greater")
# else:
#print(c,"is greater")

#ex 11
a,b,c=11,4,2023

exam_st_date =(a,b,c)
print("the exam will start from : %i / %i / %i"%exam_st_date)

#ex 12
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line\nheredoc string --------> example
""")

#ex13
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#ex14
from math import pi

#ex15
vr=4.0/3.0*pi* 6.0**3
print("the volume of sphere is : ",vr)

#ex15
num=int(input("enter any number of your choice : "))

if num > 17:
    print("num is greater than 17")
else:
    print("17 is greater")
    
#ex16
import math   
number1=int(input("give any number you want to add"))    
number2=int(input("give any number you want to add"))
number3=int(input("give any number you want to add"))

#ex 17
sum=number1 + number2 + number3
if number1==number2==number3:
    print(sum)
    sum*=3
print("the result is ",sum)   




