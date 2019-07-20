# import babel library
from babel import numbers

# create a list of numbers
l_numbers = [12000, 13000, 14000, 15003045, 45000,4839393]

# loop through list to convert each number into US Dollar currency format by using format_currency function of babel
print("Output:")
for number in l_numbers:
    formatted_n = numbers.format_currency(number, 'USD', locale='en_US')
    print(formatted_n)