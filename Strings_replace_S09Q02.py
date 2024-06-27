text = input("Enter the text to find the word: ")
sw = input("Enter the word to search in the entered text: ")
fw = input("Entert the word to be replace in the text: ")
if sw in text:
    print(text.replace(sw,fw))
