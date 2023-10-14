# https://www.practicepython.org
# Rafael Estrada Pinon. Oct 13 2023

from datetime import date

user_name = input('Give me your name: ')
user_age = int(input('Give me your age: '))
user_times_print = int(input('How many times you want to print the message?: '))

print('Your name is', user_name)
print('Your age is', user_age, '\n')

current_year = int(date.today().year)

missing_years = 100 - user_age

exact_year = current_year + missing_years

print(str('You will be 100 years old in the year ' + str(exact_year) + '\n') * user_times_print)
print('///' * 10 + '\n')
print(f'You will be 100 years old in the year {exact_year} \n' * user_times_print)



