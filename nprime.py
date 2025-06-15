while True:
    try:
        num = int(input("Enter a number = "))
        break
    except:
        print("Not a valid integer")

prime_num_counter = 0
x = 1

while prime_num_counter < num:
    counter = 0
    for i in range(1, x + 1):
        remainder = x % i
        if remainder == 0:
            counter = counter + 1    
    if counter <= 2:
        print(x)
        prime_num_counter = prime_num_counter + 1
    x = x + 1      