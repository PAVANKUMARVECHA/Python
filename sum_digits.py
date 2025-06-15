while True:
    try:
        num = int(input("Enter a number = "))
        break
    except:
        print("Not a valid integer")

while True:
    digits = list(str(num))
    sum = 0
    for digit in digits:
        sum = sum + int(digit)
    if len(str(sum)) == 1:
        print(sum)
        break
    else:
        num = sum