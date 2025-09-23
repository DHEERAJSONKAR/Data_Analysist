gender = input("enter your gender: ")
age = int(input("enter your age: "))
if age>=18 and gender == "male" or gender == "female":
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
