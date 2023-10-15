# Name - Araohat Kokate
# ID - 1001829841
# Date - 10/14/2023
# OS - Windows 11

import os

# Function to check if token is an operator
def is_operator(token):
    return token in "+-*/"

# Function to evaluate RPN expression
def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        elif is_operator(token):
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    return stack[0]

# Function to open the file and process the expression
def process_rpn_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                result = evaluate_rpn(line.strip())
                print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    # Getting directory of input file
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Making file path for input file
    file_path = os.path.join(current_dir, "input_RPN.txt")
    # Sending file for evaluation
    process_rpn_file(file_path)

