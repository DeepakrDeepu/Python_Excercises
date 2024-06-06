FN = input("Enter the file name to open:")
with open(FN, 'r') as UC:
    content = UC.read()
    print(content)
    sentences = content.split('.')
    print(sentences)
    
    capitalletter = True
    for sentence in sentences:
        if sentence and not sentence[0].isupper():
            capitalletter = False
            break
    
    if capitalletter:
        print("All Text file in the file begins with a capital letter")
    else:
        print("All Text file in the file not begins with a capital letter")    
    
        

