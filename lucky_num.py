while True:
    try:
        num = int(input("Enter a number = "))
        break
    except:
        print("Not a valid integer")

def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        rem = num % i
        if(rem == 0):
            counter = counter + 1
    if counter <= 2:
        return True
    return False

digits = list(str(num))
sum = 0
for digit in digits:
    sum = sum + int(digit)
if is_prime(sum):
    sum = 0
    for digit in digits:
        sum = sum + int(digit) ** 2
    if is_prime(sum):
        print("prime")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")