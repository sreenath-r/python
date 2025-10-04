#Datatypes

#construct 2 lists containing all the available data types (int, float, complex, bool, str, list, tuple, set, dict)
list1=[10, 20.5, 3+4j, True, "Hello", [1,2,3], (4,5,6), {7,8,9}, {"key1":"value1", "key2":"value2"}]

list2=[-5, 0.001, 2-3j, False, 'World', ['a','b','c'], (7,8), {1,2}, {"name":"Alice", "age":30}]

print(list1)
print(list2)

#create another list by concatenating above two lists
concatenated_list=list1+list2
print(concatenated_list)

#find the frequency of each element of the concatenated list
frequency_dict={}
for item in concatenated_list:
    if item in frequency_dict:
        frequency_dict[item]+=1
    else:
        frequency_dict[item]=1
print(frequency_dict)


# The above code throws error because concatenated_list contains lists, sets, and dictionaries, which are unhashable and cannot be used as dictionary keys in frequency_dict.

# To fix this, you need to only count the frequency of hashable (immutable) items, or convert unhashable items (like lists and sets) to a hashable type (like tuple or string) before using them as keys.

# Here is a modified version that only counts hashable items:
hashable_concatenated_list = []
for item in concatenated_list:
    if isinstance(item, (list, set, dict)):
        # Convert unhashable items to a string representation
        hashable_concatenated_list.append(str(item))
    else:
        hashable_concatenated_list.append(item)

# Now count the frequency of hashable items
frequency_dict = {}
for item in hashable_concatenated_list:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1
print(frequency_dict)


#create 2 sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in another set)
set1=set(range(1,11))
set2=set(range(5,16))
print(set1)
print(set2)

#find the common elements in above 2 sets
common_elements=set1.intersection(set2)
print(common_elements)

#find the elements that are not common
not_common_elements=set1.symmetric_difference(set2)
print(not_common_elements)

#remove element 7 from both sets
set1.discard(7)
set2.discard(7)
print(set1)
print(set2)

#create a dictionary of 5 states having state name as key and number of covid-19 cases as values
state_cases={
    "Andhra Pradesh": 50,
    "Telangana": 40, 
    "Kerala": 35, 
    "TamilNadu": 30, 
    "Maharashtra": 20
    }
print(state_cases)

#print only state names from the above dictionary
for state in state_cases:
    print(state)

#print only the number of covid-19 cases from the above dictionary
for cases in state_cases.values():
    print(cases)    


#update another state and its covid-19 cases to the above dictionary
state_cases["Karnataka"]=25
print(state_cases)
