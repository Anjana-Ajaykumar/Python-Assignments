import string

def count(elements, dictionary):
    # Remove punctuation like '.', ',', etc., from the word
    elements = elements.strip(string.punctuation)

    # Check if the word is already in the dictionary
    if elements in dictionary:
        dictionary[elements] += 1
    else:
        dictionary[elements] = 1

input_text = input("Enter a paragraph: ")# Get input from the user
dictionary = {}#Dictionary to store words
words = input_text.split() #Split the input into a list of words

# Process each word and update the dictionary
for word in words:
    count(word.lower(), dictionary)#Function call

# Print the frequency of each word
for word, frequency in dictionary.items():
    print(f"Frequency of '{word}': {frequency}")
