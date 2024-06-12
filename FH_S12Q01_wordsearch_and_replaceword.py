FN = input("Enter the file name to open: ")
SW = input("Enter the word to search:")
FW = input("Enter the word to repalce in the file: ")
with open(FN,'r') as file:
    for line in file:
        if SW in line:
            print(line.replace(SW,FW))
