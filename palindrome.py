word = input("Please enter a string: ")

if word == word[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
