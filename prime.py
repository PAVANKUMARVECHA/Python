while True:
    try:
        num = int(input("Enter the number = "))
        break
    except:
        print("Number should be Integer")

counter = 0

for i in range(1, num + 1):
    remainder = num % i
    if remainder == 0:
        counter = counter + 1

if counter == 2:
    print("Prime number")
else:
    print("Not a prime number")

