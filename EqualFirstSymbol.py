# Даны два слова. Проверьте, что первые буквы этих слов совпадают.

strOne = input('Введите первое слово\n')
strTwo = input('Введите второе слово\n')

if strOne[0] == strTwo[0]:
	print('Первые символы равны')
else:
	print('Первые символы не равны')
