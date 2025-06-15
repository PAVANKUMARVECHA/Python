# This practice for programming of gardation of mark list by using dictonory,if,elif and else
subject_marks = dict()

while True:
    try:
        subject_marks["telugu"] = float(input("enter the marks in Telugu = "))
        break
    except:
        print("enter the integer / float numbers")
while True:
    try:
        subject_marks["english"] = float(input("enter the marks in english = "))
        break
    except:
        print("enter the integer / float numbers")
while True:
    try:
        subject_marks["mathematics"] = float(input("enter the marks in mathematics = "))
        break
    except:
        print("enter the integer / float numbers")
while True:
    try:
        subject_marks["science"] = float(input("enter the marks in science = "))
        break
    except:
        print("enter the integer / float numbers")

while True:
    try:
        subject_marks["socialstudies"] = float(input("enter the marks in socialstudies = "))
        break
    except:
        print("enter the integer / float numbers")
    
for subject in subject_marks.keys():
    marks = subject_marks[subject]
    if marks >= 60 and marks < 70:
        print("Subject : " + subject + " Grade : C") 
    elif marks >= 70 and marks < 80:
        print("Subject : " + subject + " Grade : B")
    elif marks >= 80 and marks < 90:
        print("Subject : " + subject + " Grade : A")
    elif marks >= 90:
        print("Subject : " + subject + " Grade : Ex") 
    else:
        print("Subject : " + subject + " Grade : F") 