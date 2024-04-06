def perform_check(number):
    if 10 <= number <= 99:
        print("Entered number",number,"is a 2-Digit number")
    elif 100 <= number <= 999:
        print("Entered number",number,"is a 3-Digit number")
    else:
        print("Entered number:",number)

def get_number():   
    return int(input("Enter the numbers = "))

num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
