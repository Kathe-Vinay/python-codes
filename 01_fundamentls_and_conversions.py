# write a program to add two numbers by taking input from user

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
sum = num1+num2
print(f"sum:{num1}+{num2} = {sum}")
 
#write a program to divide two numbers by taking input from user
num1  = float(input("enter the dividend"))
num2  = float(input("enter the  divisor"))
result = num1/num2
if num1  == 0 :
    print("zero error")
else :
    print(f"result:{num1}/{num2}={result}")   

#print any random number in given range    
import random 
print(f"Random number:{random.randint(1,100)}")


#covert kilometrs to miles
kilometers = float(input("enter distance in kilometers"))
# 1 kilometer = 0.621371
conversion_factor = 0.621371
result = kilometers*conversion_factor
print(f"conversion_factor={kilometers}*{conversion_factor}={result}")

#convert celsius to fahreinheit
celsius = float(input("enter temperature in celsius "))
#fahrenheit = (celsius*9/5)+32
fahrenheit = (celsius*9/5)+32
print(f"fahreinheit:{fahrenheit}")

#print calander of year and month given by user
import calendar
year =int (input("enter the year"))
month =int(input("enter the month"))
cal = calendar.month(year,month)
print(cal)

#finding roots of given quadratic equation
import math
a = float(input("enter the first number"))
b = float(input("enter the second number"))
c = float(input("enter the third number"))
discriminant =(b**2)-4*a*c
if  discriminant > 0 :
    root1 = -b + math.sqrt(discriminant)/2*a
    root2 = -b - math.sqrt(discriminant)/2*a
    print(f"Root1={root1}")
    print(f"Root2={root2}")
elif discriminant == 0 :
    root = -b/2*a
    print(f"Root = {root}")   
else :
    real_part = -b/2*a
    imaginary_part = math.sqrt(abs(discriminant))/2*a
    print(f"Root1 = {real_part}+{imaginary_part}i")
    print(f"Root2={real_part}-{imaginary_part}i")    

# swap integers without using temp
a = 10
b = 5
a,b = b,a
print("after swapping")
print("a=",a)
print("b=",b)

#check whether a given number is positive or negative
num = int(input("enter a number"))
if num>0:
    print("given number is positive")
else:
    print("given number is negative")
    

