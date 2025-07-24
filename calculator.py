# Basic Calculator

#Number input
first_number = input('Enter your first number:')
second_number = input('Enter your second number:')

# Operation type input
operation_type = input('Operation type: Enter +, -, * or / :')

# Calculation
if operation_type == '+':
    result = int(first_number) + int(second_number)
    print(f'Addition is {result}')
elif operation_type == '-':
    result = int(first_number) - int(second_number)
    print(f"Subtraction is {result}")
elif operation_type == '*':
    result = int(first_number) * int(second_number)
    print(f"Multiplication is {result}")
elif operation_type == '/':
    result = int(first_number) / int(second_number)
    print(f"Division is {result}")
else:
    print('Enter valid operation type')