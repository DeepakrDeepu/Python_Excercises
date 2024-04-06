def One_digit_oper(number):
    result = number + 7
    return result % 10

def Two_digit_oper(number):
    result = number ** 5
    return result % 10

def Three_digit_oper(number, number2):
    result = number + number2
    return result % 10

def perform_check(number):
    if 0 <= number <= 9:
        return One_digit_oper(number)
    
    elif 10 <= number <= 99:
        return Two_digit_oper(number)
    
    else:
        number2 = int(input("Enter the second number = "))
        return Three_digit_oper(number, number2)
    
number = int(input("Enter the number = "))
final_result = perform_check(number)
print("final_result:",final_result)
