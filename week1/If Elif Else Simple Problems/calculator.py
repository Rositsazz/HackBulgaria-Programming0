number1 = input ('Enter first number: ')
number2 = input ('Enter second number: ')

number1 = int(number1)
number2 = int(number2)

oper = input('Enter an operator(choose from +, -, * or /)')
if oper == '+':
    print(number1+number2)

elif oper == '-':
    print(number1-number2)

elif oper == '*':
    print(number1)*number2)

elif oper == '/':
    print((number1)/number2)
    
else:
    print('We do not support that operation.')
