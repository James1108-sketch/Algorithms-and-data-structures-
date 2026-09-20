def balanced_paratheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return not stack

text = input("Enter a string of parentheses: ")
if balanced_paratheses(text):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")