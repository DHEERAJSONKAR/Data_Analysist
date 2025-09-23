# a = 1 
# match a:
#     case 1:
#         print("valid input")
#     case _:
#         print("invalid input") 
# day = input("Enter your days: ")
# match day:
#     case "Monday" | "monday":
#         print("monday")
#     case "Tuesday" |"tuesday":
#         print("tuesday")
#     case "Wednesday"|"wednesday":
#         print("wdnesday")
#     case "Thursday"| "thrusday":
#         print("thursday")
#     case "Frinday" | "friday":
#         print("friday")
#     case "Saturday" | "saturday":
#         print("saturday")
#     case "Sunday" | "sunday":
#         print("sunday")
#     case _:
#         print("This is your day.")
a =float(input("Enter your first number: "))
b =float(input("Enter your second number: "))
opr = input("Enter your operation(+,-,*,/): ")
match opr:
        case "+":
            print("sum is two number: " , a + b)
        case "-":
            print("difference is two number: " , a - b)
        case "*":
            print("multiply is two number: " , a*b)
        case "/":
            print("division is two number: " , a/b)
        case _:
            print("this is default value.")