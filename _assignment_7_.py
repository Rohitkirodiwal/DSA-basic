#7. Write a program to convert prefix expression to infix expression.

def is_operator(char):
    operators = set(['+', '-', '*', '/', '^'])
    return char in operators

def prefix_to_infix(prefix_expression):
    stack = []
    
    for char in reversed(prefix_expression):
        
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = "(" + operand1 + char + operand2 + ")"
            stack.append(infix_expression)
    
    return stack.pop()

prefix_expression = "*+23/45"
infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)