#Palindrome checker to check given string is palindrome

string = input("Enter a string: ").replace(" ","")  #ignore spaces
rev=string[::-1]
print("Reverse :",rev.lower())

if(string.lower()==rev.lower()):    #ignore cases
    print("\nGiven string is a palindrome")
else:
    print("\nGiven string is not a palindrome")
