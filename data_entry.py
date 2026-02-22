# Prompt the user to enter a sentence and then print the sentence in uppercase letters.

# Prompt the user to enter a paragraph and then count the number of words in the paragraph.

# Prompt the user for a string, and check if all the characters in the string are digits. Output true or false

# Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".

# Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.

# Prompt the user for a string, then print its length.

sentence=input("Write a sentence: ")
print(sentence.upper())

sentence=input("Write a sentence: ")
print(len(sentence))

word="youtube"
print(word.isdigit())

word2=input("Enter a word that start with an a: ").replace("a","o")
print(word2)

first_name=input("Enter your first name: ")
last_name=input("Enter your first name: ")
print(first_name[0] + last_name[0])

word3=input("Enter a word: ")
print(len(word3))
