def sum(number1, number2, number3):
    result = number1 + number2 + number3

    if number1 == number2 == number3:
        return number1 * number2 * number3
    elif number1 == number3:
        return number1 * number3 + number2
    elif number1 == number2:
        return number1 * number2 + number3
    elif number2 == number3:
        return number2 * number3 + number2
    else:
        return result




number1 = eval(input("Enter First Number: "))
number2 = eval(input("Enter Second Number: "))
number3 = eval(input("Enter Third Number: "))

total = sum(number1, number2, number3)

print("The result is:", total)



