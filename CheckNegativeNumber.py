#Check

def check_negative_number (number):
    if number > 0:
        print ('This number is positive')
    elif number < 0:
        print('This number is negative')
    elif number == 0:
        print('This number is zero')
    else:
        print('This number is wrong')

number = int(input('Write you number\n'))

check_negative_number(number)