num = int(input("Enter the number:"))
if 0 <= num <= 9:
    result = num + 7
    print("Addition of the one digit number with 7 & printing it's units place value: {} + 7 = ".format(num), result % 10)
elif 10 <= num <= 99:
    result = num ** 5
    print("The Power of two digit number & printing it's last two digit's values:{} ** 5 = ".format(num), result % 100)
elif 100 <= num <= 999:
    Another_number = int(input("Please enter another number: "))
    result = num + Another_number
    print(" Addition of num & Another number to print the last 3 digits values: {} + {} = ".format(num, Another_number), result % 1000)
    
