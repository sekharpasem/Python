# import babel library
from babel import numbers

# my initial string with unformatted numbers
s1 = "What the provider charged: 493555555555.0\nWhat Anthem allowed:  59494930.0\nWhat Anthem paid: 0.0\nIn-Network discount: 493.0 \nWhat the member owes: 0.0\nDeductible amount 0.0\nCoinsurance amount 0.0\nCopayment amount 0.0\nNon-eligible charges 0.0\nWhat Medicare allowed: 0.0\nWhat Medicare paid: 0.0"

# temporary list to store elements
l = []

# function which will take number and converts into readable format
def format_currency(math_value):
    """

    :param math_value:
    :return:
    """
    return str(numbers.format_currency(math_value, 'USD', locale='en_US'))

# I want to use split functionality with space, so that I can get words and numbers to convert
for t in s1.split():

    try:
        # convert string number to float, raises ValueError when string is not number, so we don't to convert
        n = float(t)
        # gets readable format number back
        s = format_currency(n)
        # appending number to list, so that we construct final as it string with formatted numbers
        l.append(s)
        l.append("\n")
    except ValueError:
        l.append(t)

# lastly, join each word in the list with space, so it will become our final string
strr  = " ".join(l)
print(strr)