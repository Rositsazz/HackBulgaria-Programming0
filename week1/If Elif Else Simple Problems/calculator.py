number1 = input ('Enter first number: ')
number2 = input ('Enter second number: ')
oper = input('Enter an operator(choose from +, -, * or /)')
if oper == '+':
    print(int(number1)+int(number2))
elif oper == '-':
    print(int(number1)-int(number2))
elif oper == '*':
    print(int(number1)*int(number2))
elif oper == '/':
    print(int(number1)/int(number2))
else:
    print('We do not support that operation.')
