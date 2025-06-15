# while True:
#     try:
#         b=float(input("Enter the Base of the triangle: "))  
#         break
#     except:
#         print("Base whould be of Numeric Type")

# while True:
#     try:
#         h=float(input("Enter the height of the triangle: "))
#         break
#     except:
#         print("Height whould be of Numeric Type")
                
# area=(b*h)/2
# print("area of the triangle = " + str(area))

for i in range(2):
    try:
        b=float(input("Enter the Base of the triangle: "))  
        break
    except:
        print("Base whould be of Numeric Type")
        
for i in range(2):
    try:
        h=float(input("Enter the height of the triangle: "))
        break
    except:
        print("Height whould be of Numeric Type")

try:
    area=(b*h)/2
    print("area of the triangle = " + str(area))
except NameError:
    print("Base or Height or Both might not be of Numeric Type")
except TypeError:
    print("TypeError")