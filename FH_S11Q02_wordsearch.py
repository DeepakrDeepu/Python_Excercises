FN = input("Enter the file name to open: ")
SW = input("Enter the word to search:")
with open(FN,'r') as file:
    for line in file:
        if SW in line:
            print(line)
            
