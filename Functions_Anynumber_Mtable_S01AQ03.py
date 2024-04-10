# Print the multiplication table using any number using function

def print_mtable():
    Mul_num = int(input("Enter the Multiplication table value: "))
    for num in range(1, 11):
        Table = Mul_num * num
        print(Mul_num,"*",num,"=",Table)
        num += 1
        
print_mtable()
