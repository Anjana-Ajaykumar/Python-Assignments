#Dictionary Sorter

#accepts dictionary from user
user_dict=eval(input("Enter a dictionary :\n"))
#sorts the dictionary in ascending order
sorted_dict=dict(sorted(user_dict.items()))
print("Sorted list is :")
print(sorted_dict)
