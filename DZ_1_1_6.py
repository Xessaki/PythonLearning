
# Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, 
# то получите предпоследнюю букву.

strOne = input('Введите слово:\n')
if strOne[-1] == 'ь':
	print(strOne[-2])
else:
	print(strOne[-1])