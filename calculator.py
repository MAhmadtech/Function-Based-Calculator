# """
# Write a code to make a simple calculator ,
# Instruction:
# 1: input first number from user 
# 2: input second number from user
# 3: select symbol of (+,-,/,*)
# 4: print the output ...
# """


num1=float(input("Enter the first number:"))

num2= float(input("Enter the second number:"))

operator=input("choose an operation (+,-,*,/): ")

if operator == '+':
  result = int(num1 + num2)
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result =  num1 * num2
elif operator  == '/' and num2 != 0:
    result = num1 / num2
else:
  print("Invalid operator. Please choose +, -, *, or /.")

if num2 != 0:
  print(f"{num1} {operator} {num2} is equal to {result}")
else:
  print("Error: Division by zero is not allowed.")
