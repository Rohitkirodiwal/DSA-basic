#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def check_bracket(code):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in code:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            check = stack.pop()
            if brackets[check] != char:
                return False

    return not stack

code = "(a +[c+d]+a)"

if check_bracket(code):
    print("All brackets are closed in the code snippet.")
else:
    print("Not all brackets are closed in the code snippet.")