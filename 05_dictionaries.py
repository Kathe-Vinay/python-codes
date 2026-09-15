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
