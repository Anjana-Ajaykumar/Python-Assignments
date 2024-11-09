# Python program to illustrate string with unique characters
def uniqueCharacters(str):
    # If at any time we encounter 2 same characters, return false
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    # If no duplicate characters encountered, return true
    return True

string = input("Enter a string:")
str=string.lower()
if(uniqueCharacters(str)):
    print("True\nThe string ", string," has all unique characters")
else:
    print("False\nThe string ",string," has duplicate characters")
