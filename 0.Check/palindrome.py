#This program checks if the number / string is palindrome or not

def is_palindrome(phrase):
	print(phrase)
	phrase=phrase.lower()
	clear_phrase="".join(char for char in phrase if char.isalnum())
	return clear_phrase==clear_phrase[::-1]

#Direct
print("Brute check")
print("->",is_palindrome("A man, a plan, a canal: Panama"))
print("->",is_palindrome("This is a dog"))

#User input
uinp=input("Enter a string or a number: ")
print("->",is_palindrome(uinp))



