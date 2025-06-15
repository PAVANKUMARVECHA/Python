while True:
    try:
        num = int(input("enter the integer number = "))
        break
    except:
        print("Not an integer number")
remainder = num % 2
if remainder == 0 :
    print("even")
else:
    print("odd")
    