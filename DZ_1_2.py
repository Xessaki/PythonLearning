# Дано число. Выведите в консоль первую цифру этого числа.

number = 103
number = str(number)
print(number[0])

# Дано число. Выведите в консоль последнюю цифру этого числа.

number = 103
number = str(number)
print(number[-1])

# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.

number = 103
number = str(number)
Sum = int(number[0]) + int(number[-1])
print(Sum)

# Дано число. Выведите количество цифр в этом числе.

number = 103
number = str(number)
print(len(number))

# Дан список: [1, 2, 3, 4, 5, 6] получить из него срез: [1, 2, 3]
l = [1, 2, 3, 4, 5, 6]
print(l[0:3])