marks = int(input("Please enter your marks.:"))

if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("You are average students")

if marks % 2 == 0:
    print("marks is even")
else:
    print("marks is odd")

