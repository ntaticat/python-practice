# https://www.practicepython.org
# Rafael Estrada Pinon. Oct 13 2023

user_number = int(input('Give me an integer number: '))
user_divider = int(input('Give me an integer number to divide the previous number: '))

if user_number % 4 == 0:
    print('The given number is multiple of Four')
elif user_number % 2 == 0:
    print('The given number is Even')
else:
    print('The given number is Odd')

if user_number % user_divider == 0:
    print('The division between the numbers is evenly')
else:
    print('The division between the numbers is not evenly')
