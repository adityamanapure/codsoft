# Task 2 -Calculator

def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result =  n1*n2
    elif op == '/':
        result = n1/n2
    elif op=='^':
        result =  n1**n2
    else:
      print('You have not typed a valid operator, please run the program again!!!')
        
    return result

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
op = input('Enter operator (+,-,*,/,^): ')
result=calculate(number1,number2,op)
print(number1,op,number2,'=',result)
