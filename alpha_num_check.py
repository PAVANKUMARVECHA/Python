password = list(input(" enter the password = "))
counter = dict()
counter['small'] = 0
counter['big'] = 0
counter['numbers'] = 0
counter['special charcters'] = 0

for char in password:
    if char.islower():
        counter['small'] = counter['small'] + 1
    elif char.isupper():
        counter['big'] = counter['big'] + 1
    elif char.isnumeric():
        counter['numbers'] = counter['numbers'] + 1
    else:
        counter['special charcters'] = counter['special charcters'] + 1

print(counter)

