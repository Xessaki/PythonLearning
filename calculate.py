#My First app Calculator

print('Привет, добро пожаловать в мою первую программу!')
print('Да, это всего лишь калькулятор, но все с чего-то начанали :)')
print()

firstNumber = int(input('Введите первое число:\n'))
secondNumber = int(input('Введите второе число:\n'))
operation = input('Какое действие совершить с числами?\n')

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


print('Ваш ответ: ' + str(calculate(firstNumber, secondNumber, operation)))

