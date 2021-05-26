word = input("Enter a string ")

if word == word[::-1]:
    print("it is a palindrome")
else:
    print("it is not palindrome")