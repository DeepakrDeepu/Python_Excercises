# Multiplication table code using for loop

num = int(input("Enter the Multiplication number: "))
#for i in range(1,11):
#    Mul = num * i
#    print(num,'*',i,'=',Mul)
    
# Multiplication table using while loop
i = 1
while i <= 10:
    Mul = num * i
    print(num,'*',i,'=',Mul)
    i = i + 1
