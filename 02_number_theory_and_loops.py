#check whether a given number is prime or not
num = int(input("enter the number"))
flag = False

if num == 1:
    print(f"{num} , is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            flag = True
            break

if flag:
    print(f"{num},is not a prime number")
else:
    print(f"{num},is a prime number")

#print prime numbers in given range
lower = 1
upper = 20
print("prime numbers betwwen",lower,"and",upper)
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num)

#print factorial of given number
num = int(input("enter the number"))
factorial = 1
if num < 0:
    print(" no factorial for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):

        factorial = factorial*i
        print(factorial)
#display the multiplication table for a given number in given range
num = int(input("display multiplication of "))
for i in  range(1,11):
    print(f"{num}*{i}={num*i}")

#fibonacci series
nterms = int(input("enter the number of terms"))
n1,n2 = 0,1
count = 0 

if nterms<= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("fibonacci sequence of 1 is") 
    print(n1)   
else:
    print("fibonacci sequence of given number is:")
    while count < nterms:
       print(n1)
       nth = n1+n2
       n1 = n2
       n2 = nth
       count += 1 

#armstrong number
num = int(input("enter the number"))

num_str = str(num)
num_digits = len(str(num))

sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num%10
    sum_of_powers += digit**num_digits
    temp_num //= 10

if sum_of_powers == num :
    print("is armstrong")
else:
    print("is not armstrong")      


#armstrong numbers in given range
lower = int(input("enter the lower limit"))
upper = int(input("enter the upper limit"))

for num  in range(lower,upper+1):
    order = len(str(num))
    temp_num = num
    sum_of_powers = 0

    while temp_num>0:
        digit = temp_num%10
        sum_of_powers+=digit**order
        temp_num//=10

    if sum_of_powers == num:
     print(f"{num}is armstrong")

limit =int(input("enter the limit"))
sum = 0
for i in range(1,limit+1):
    sum+=i
print("the sum of natural numbers upto",limit,"is",sum)  

#lcm of given number
def compute_lcm(x,y):
    if x>y :
     greater = x
    else:
     greater = y
    while(True):
      if(greater%x==0) and (greater%y==0):
         lcm = greater
         break;
      greater+=1
    return lcm
num1 = int(input("enter the number 1"))
num2 = int(input("enter the number 2"))    
print(f"the lcm of given numbers{num1} and {num2}is",compute_lcm(num1,num2))

#hcf of given number
def compute_hcf(x,y):
    if x>y:
       smaller = y
    else:
       smaller = x
    for i in range(1,smaller+1):
       if(x%i==0) and (y%i==0):
          hcf = i
    return hcf
num1 = int(input("enter the 1st number:"))
num2 = int(input("enter the 2nd number"))
print("hcf of given 2 numbers is",compute_hcf(num1,num2))       


#disarium number
def is_disarium(number):

    num_str = str(number)

    digit_sum = sum(int(i)**(index+1) for index, i in enumerate(num_str))

    return digit_sum == number

num = int(input("enter a number"))

if is_disarium(num):
    print ("is disarium")
else:
    print ("not disarium")    

#printing diarium numbers in given range
def is_disarium(number):

    num_str = str(number)

    digit_sum = sum(int(i)**(index+1) for index , i in enumerate(num_str))

    return digit_sum==number
disarium = [num for num in range(1,101) if is_disarium(num)]
print("Disarium numbers are :")
for num in disarium:
    print(num, end="|")



#happy number
def is_happy_number(num):
    seen = set()
    while num!=1 and num not in seen:
        seen.add(num)
        num = sum(int(i)**2 for i in str(num))
    return num ==1

num = 24
if is_happy_number(num):
    print(num,"is happy number")
else:
    print("not happy number")        


#harshad number
def is_harshad_number(num):
    digit_sum = sum(int(i) for i in str(num))

    return num%digit_sum ==0

num = int(input("enter a number"))

if is_harshad_number(num):
    print(num,"is harshad number")
else:
    print(num,"is not harshad number")    



#pronic number
def is_pronic_number(num):
    for n in range(1,int(num**0.5)+1):
        if n*(n+1)==num:
            return True
    return False
print("pronic numbers between 1 to 100 : ")
for i in range(1,101):
    if is_pronic_number(i):
        print(i,end="|")    

#sum of cube of fisrt n natural numbers
def sum_of_cube_of_n_natural_numbers(n):
    if n<=0:
        return 0
    else:
        total = sum(i**3 for i in range(1,n+1))
        return total
n = int(input("enter the number"))
if n < 0:
    print("please enter positive integer")
else:
    result = sum_of_cube_of_n_natural_numbers(n)
    print("the sum of n natural numbers is:",result)        




