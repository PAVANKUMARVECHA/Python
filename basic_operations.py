while True:
    try:
        num1 = float(input("enter the 1st number : "))
        break
    except:
        print("num1 should be a numeric type")
while True:
    try:
        num2 = float(input(" enter the 2nd number = "))
        break
    except:
        print("num2 should be a numeric type")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2
print("Addition = "+ str(addition))
print("Subtraction = " + str(subtraction))
print("multiplication = " + str(multiplication))
print("divison = " + str(division))
print("remainder = " + str(remainder))
