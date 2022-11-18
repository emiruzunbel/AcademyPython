number1 =23
number2 =12
number3 =7

if number1>number2 and number1>number3:
    if number2>number3:
        print(f"{number1} is greater value and {number3} is smaller value")
    else:
        print(f"{number1} is greater value and {number2} is smaller value")
elif number2>number1 and number2>number3:
    if number1>number3:
        print(f"{number2} is greater value and {number3} is smaller value")
    else:
        print(f"{number2} is greater value and {number1} is smaller value")
elif number3>number1 and number3>number2:
    if number1>number2:
        print(f"{number3} is greater value and {number2} is smaller value")
    else:
        print(f"{number3} is greater value and {number1} is smaller value")
else:
    print("Values are equal.")
