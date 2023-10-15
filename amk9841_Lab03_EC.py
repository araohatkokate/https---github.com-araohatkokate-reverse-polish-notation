# Name - Araohat Kokate
# ID  - 1001829841
# Date - 10/14/2023
# OS - Windows 11

import os

# Precedence of operators along with unary subtraction
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '-u': 3}

# Function to convert an algebraic expression to RPN
def algebraic_to_rpn(expression):
    output = []
    operator_stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Remove the left parenthesis
        elif token in "+-*/-u":  # Added -u for unary subtraction
            while (operator_stack and operator_stack[-1] in "+-*/-u" and
                   precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                output.append(operator_stack.pop())
            operator_stack.append(token)
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return ' '.join(output)

# Function to evaluate an RPN expression
def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        elif token == '-u':
            if len(stack) < 1:
                raise ValueError("Invalid RPN expression")
            operand = stack.pop()
            stack.append(-operand)
        elif token in "+-*/":
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                stack.append(a / b)
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    return stack[0]

# Function to open the file and process the expression 
def process_algebraic_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                algebraic_expression = line.strip()
                rpn_expression = algebraic_to_rpn(algebraic_expression)
                result = evaluate_rpn(rpn_expression)
                print("Algebraic Expression: ", algebraic_expression)
                print("RPN Expression: ", rpn_expression)
                print("Result: ", result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    # Getting directory of input file
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Making file path for input file
    file_path = os.path.join(current_dir, "input_RPN_EC.txt")
    # Sending file for evaluation
    process_algebraic_file(file_path)
