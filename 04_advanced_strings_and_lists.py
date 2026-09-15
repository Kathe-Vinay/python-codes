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
           
