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
fahrenheit = (celsius*9/5)+322
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

#converting a decimal number into binary, octal,hex
dec_num = int(input("enter a decimal number:"))

print("The decimal value of", dec_num,"is")
print(bin(dec_num),"in binary")
print(oct(dec_num),"in octal")
print(hex(dec_num),"in hexa decimal")

#printing ascii value 
char = str(input("enter the character:"))
print("the ascii value of ", char , ord(char))

# mini calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while(True):
    choice = input("enter choice 1/2/3/4")

    if choice in('1' '2' '3' '4' '5'):
       try:
           num1 = float(input("enter the 1st number:"))
           num2 = float(input("enter the 2nd number:"))
       except ValueError:
           print("invalid input.please enter a number")
           continue
       if choice=='1':
           print(num1,"+",num2, "=",add(num1,num2))
       elif choice=='2':
         print(num1,"-",num2,"=",sub(num1,num2))
       elif choice=='3':
           print(num1,"*",num2,"=",multiply(num1,num2))
       elif choice=="4":
           print(num1,"/",num2,"=",divide(num1,num2))    

       next_calculation = input("lets do calculation?(yes/no)")
       if next_calculation=="no":
         break
    else:
        print("invalid input")   

#factorial using recursion
def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
print (factorial(5))    


#fibonacci using recursion
def recur_fibo(n):
    if n<=1:
       return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

terms = int(input("number of terms"))

if terms<0:
    print("give only positive numbers ")
else:
    for i in range(0,terms+1):
        print(recur_fibo(i))    



#sum of cube of natural numbers in given range
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


#to find largest element in an array
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]

    for element in arr:
        if element>largest_element:
            largest_element=element
    return largest_element 
my_array = [10,40,50,20]
result = find_largest_element(my_array)
print(f"the largest element in array is: {result}")


# rotating an array
def rotate_array(arr,d):
    n = len(arr)

    if d<0 or d>=n:
        return "invalid rotation value"

    rotated_arr = [0] *n

    for  i in range(n):
        rotated_arr[i] = arr[(i+d)%n]

    return rotated_arr
arr = [1,2,3,4,5]

d = 2

result = rotate_array(arr,d)

print("original array:",arr)
print("rotated array:",result)

#splitting and adding array
def split_and_add(arr,k):
    if k<=0 or k>=len(arr):
        return arr

    first_part = arr[:k]
    second_part =arr[k:]


    result = second_part+first_part

    return result
arr = [1,2,3,4,5]
k=3
result=split_and_add(arr,k)
print("original array:",arr)
print("array after splitting and adding:",result)


#checking whether the given array is monotonic or not
def is_monotonic(arr):
    increasing = decreasing=True

    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            decreasing = False
        elif arr[i]<arr[i-1]:
            increasing=False

    return increasing or decreasing    
arr1 = [1,2,3,4]
arr2 = [3,2,1]
arr3 = [1,3,2,4]
print(is_monotonic(arr1))
print(is_monotonic(arr2))
print(is_monotonic(arr3))




#addition of matrices
def add_matrices(mat1,mat2):
    if len(mat1)!=len(mat2):
        return "matrices must have the same dimensions for addition"

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
            result.append(row) 

        return result

matrix_1 =  [

    [1,2,3],
    [4,5,6],
    [7,8,9]
]         
matrix_2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
result_matrix = add_matrices(matrix_1,matrix_2)

print(result_matrix)


#multiplication of matrices
def multiply_matrices(matrix_1,matrix_2):
    rows1 = len(matrix_1)
    cols1 = len(matrix_1[0])
    rows2 = len(matrix_2)
    cols2 = len(matrix_2[0])

    if cols1 != rows2:
        return "matrix multiplication is not possible"

    result =[[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += matrix_1[i][k]*matrix_2[k][j]
    return result

matrix_1 = [
    [1,2,3,],
    [4,5,6]
]

matrix_2 = [
    [7,8],
    [9,10],
    [11,12]
]

result_matrix = multiply_matrices(matrix_1,matrix_2)
print(result_matrix)


#sorting words
my_string = (input("enter a string"))

words = [word.capitalize() for word in my_string.split()]

words.sort

print("the sorted words are")
for word in words:
    print(word)


#removing punctuations from a sentence
punctuations = '''~!@#$%^&*()_-+={}[]:;<,>.?/'''
my_str = input("enter a string")

no_punct =""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct+char
print(no_punct)

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

#sum of numbers in the list
numbers = [10,20,30,40,50]

sum_of_numbers = 0

for i in numbers:
    sum_of_numbers += i

print("sum of elements in list :",sum_of_numbers)    


#product of numbers in the list
numbers = [10,20,30,40,50]

product_of_numbers = 1

for i in numbers:
    product_of_numbers*=i

print("product of elements in the list",product_of_numbers)


#finding smallest number in the list
numbers = [10,30,45,-40,60]
minimum_numbers =numbers[0]

for i in numbers:
    if i< minimum_numbers:
       minimum_numbers=i
print("the smallest number in the lists is",minimum_numbers)       

#finding second largest element
numbers = [10,60,90,159,132]
numbers.sort(reverse=True)

if len(numbers)>=2:
    second_largest = numbers[1]
    print("the second largest number in list", second_largest)
else:
    print("no second largest")    

# finding n largest numbers
def find_n_largest_elements(lst,n):
    sorted_list = sorted(lst,reverse=True)

    largest_elements = sorted_list[:n]

    return largest_elements
numbers = [30,10,20,40,50,69,300,500]
n = int(input("enter number of elements"))

result = find_n_largest_elements(numbers,n)

print(f"the {n} largest elements in the list are:", result)


# program to even numbers from a list using list comprehension
numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = [num for num in numbers if num%2==0]
print("even numbers in list:",even_numbers)


#removing all empty lists
list_of_lists = [[1,2,3],[],[4,5],[],[6,7,8],[]]

filtered_list = [i for i in list_of_lists if i]

print("lists after removing empty lists:",filtered_list)




# write a program to clone a list using slicing
original_list = [10,20,30,40,50]
cloned_list = original_list[:]
print(cloned_list)



#program to clone a list using list() function 
original_list = [10,20,30,40,50]
cloned_list = list(original_list)
print(cloned_list)

#program to clone a list using list comprehension
original_list = [1,2,3,4,5]
cloned_list = [item for item in original_list]
print(cloned_list)

#counting a particular element in list
def count_occurences(l,element):
    count = l.count(element)
    
    return count
my_list = [1,2,3,4,2,5,2,3,4,6,5]
element_to_count = 2 

occurences = count_occurences(my_list,element_to_count)
print(element_to_count,occurences)

#program to find words that are longer than a given range
def fine_words(words,k):
    result= []

    for i in words:
        if len(i)>k:
            result.append(i)
    return result
words_list = ["apple","banana","cherry","date"]
k=5
long_words = fine_words(words_list,k)
print(f"words longer than {k} characters: {long_words}")       

#skipping character from a string using slicing technique
def remove_char(input_str,i):
    if i<0 or i>len(input_str):
        print(f"{i} is  invalid for given string ")
        return input_str
    result_str = input_str[:i]+input_str[i+1:]
    return result_str
my_string = "Hello, wWorld"
i = 7
my_result = remove_char(my_string,i)
print(my_result)

## program to split and join a string
input_str = "python program to split and join a string"
word_list = input_str.split()

seperator = " "
output_str = seperator.join(word_list)

print("original string:",input_str)
print("list of split words:",word_list)
print("joined string:",output_str)


#checking whether the given value is binary or not
def is_binary(input_str):
    for i in input_str:

        if i not in '01':
            return False
    return True
input_str = "101101"

if is_binary(input_str):
    print(f"{input_str} is a binary string")
else:
    print(f"{input_str} is not binary string")    


#finding symmetric differnce among two strings
def uncommon_words(str1,str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words_set = words1. symmetric_difference(words2)
    uncommon_words_list = list(uncommon_words_set)

    return  uncommon_words_list

string1 = "this is first thing"
string2 = "this is second thing"

uncommon = uncommon_words(string1,string2)
print(uncommon)


#program to find duplicate charcters in a string
def find_duplicates(input_str):
    char_count = {}

    duplicates = []

    for i in input_str:

        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i] = 1

    for i,count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
input_string = "piush sharma"

duplicate_chars = find_duplicates(input_string)

print("duplicate characters:",duplicate_chars)


#program to find whether a string contains special charcters by using regular expression
import re
def check_special_char_in_string(input_str):
    pattern = r'[~`!@#$%^&*()_+-={}:"<>?,./]'
    if  re.search(pattern,input_str):
        return True
    else:
        return False
in_string = str(input("enter a string"))
contains_special_char = check_special_char_in_string(in_string)
if contains_special_char:
    print("the string contain special characters")
else:
    print("the string have no special characters")        
           


#program to extract unique values from a dictionary
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':30,
    'e':40
}
unique_val = set()
for i in my_dict.values():
    unique_val.add(i)
unique_val_list = list(unique_val)
print("unique value from the given dictionary:",unique_val_list)    



#program to merge two dictionaries
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

dict1.update(dict2)

print("merged dictionary (using update()):",dict1)

# To merge two dictionaries using** operator(unpacking)

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
merged_dict = {**dict1,**dict2}

print("merged dictionary:",merged_dict)

#program to convert list of tuples into a dictionary
key_value_list = [('a',1), ('b',2),('c',3),('d',4)]

flat_dict = {}

for key, values in key_value_list:
    flat_dict[key]= values

print("flat dictionary:", flat_dict)

