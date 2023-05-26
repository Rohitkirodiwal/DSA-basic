#6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression

def postfix_to_prefix(postfix_expression):
    stack = []
    
    for char in postfix_expression:
        
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = char + operand1 + operand2
            stack.append(prefix_expression)
    return stack.pop()

postfix_expression = "23+4*5/"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)