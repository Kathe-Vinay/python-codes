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






