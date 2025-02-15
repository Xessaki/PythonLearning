#My First app Calculator

print('Привет, добро пожаловать в мою первую программу!')
print('Да, это всего лишь калькулятор, но все с чего-то начанали :)')
print()

print('Введите первое число: ')
firstNumber = int(input())
print('Введите второе число: ')
secondNumber = int(input())
print('Какое действие совершить с числами?')
operation = input()

# Функция калькульяторп
def calculate(firstNumber, secondNumber, operation):
    if operation == '+':
        result = firstNumber + secondNumber
        return result
    elif operation == '-':
        result = firstNumber + secondNumber
        return result
    elif operation == '*':
        result = firstNumber * secondNumber
        return result
    elif operation == '/':
        result = firstNumber / secondNumber
        return result
    else:
        print('Данная операция не поддерживается')


print(calculate(firstNumber, secondNumber, operation))

