Source = input('Enter the file name to open: ')

with open(Source) as SF:
    content = SF.read()
    print(content)
    sentences = content.split(' ')

with open('copycontent.txt', 'w') as DF:
    for sentence in sentences:
#        sentence = sentence.strip()
        DF.write(sentence + '\n')

with open('copycontent.txt', 'r') as DF:
    print('Display the copied content stored on a new line:', DF.read())
        
