# Print the multiplication table using function

def print_mtable():
    num = 1
    Mul_num = 17
    while num <= 10:
        Table = Mul_num * num
        print(Mul_num,"*",num,"=",Table)
        num += 1
        
print_mtable()
