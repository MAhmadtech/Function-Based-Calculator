from function_calculator_call import addition,sub,multi,divide,power,sqr
while True:
    num1 = float(input("Enter your first number :"))
    num2 = float(input("Enter the second number :"))
    print(""" +: for adding of two number.
          -: for subtracting of two number.
          *: for multiplaying of two number.
          /: for dividing of two number.
        pow: for power of two numbers.
     square: for square of two numbers. """)
    operator = input("Choose an operations +,-,*,/, pow,square :")

    if operator  == '+':
        print(addition(num1, num2))
    if operator == '-':
        print(sub(num1,num2))
    if operator == '*':
        print(multi(num1,num2))
    if operator == '/':
        print(divide(num1,num2))
    if operator == 'pow':
       print(power(num1,num2))  
    if operator == 'square':
        print(sqr(num1)) 
    choice = input("Do you want to continue? (Y/N): ")
    if choice.lower() == 'n':
        break
    
