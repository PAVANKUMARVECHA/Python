# This practice is for mathematical functions



while True:
    try:
        num1 = float(input(" enter the 1st number = "))
        break
    except:
        print(" enter the correct integer/float number")
while True:
    try:
        num2 = float(input(" enter the 2nd number =" ))
        break
    except:
        print(" enter the correct integer/float number") 
while True:
    try:
        num3 = float(input( "enter the 3rd number =" ))
        break
    except:
        print(" enter the correct integer/float number") 
addition = num1 + num2 + num3
subtraction = num1 - num2 - num3
multiplication = num1 * num2 * num3
division = num1 / num2 / num3
remainder1 = num1 % num2  
remainder2 = num2 % num3
print( " addition of 3 numbers = " + str(addition))
print( " subtraction of 3 numbers = " + str(subtraction))
print( " multiplication of 3 numbers = " + str(multiplication))
print( " division of 3 numbers = " + str(division))
print( " remainder1 of 1st 2 numbers = " + str(remainder1))
print( " remainder2 of next 2 numbers = " + str( remainder2))

