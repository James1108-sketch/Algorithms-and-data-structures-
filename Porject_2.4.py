def palindrome_generator(txt):
    reverse=""
    for char in txt:
        reverse = char + reverse
    return txt + reverse

txt = input("enter a string: ")
palindrome = palindrome_generator(txt)
print("Palindrom: ", palindrome)