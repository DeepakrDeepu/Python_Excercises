sen = input("Enter a long sentence: ")
print('The last character in the sentence:', sen[-1])
print('The 5 characters in the sentence are:', sen[-5:])
print('The characters which are present in the 2nd Position & 5th Position is: {} & {}'.format(sen[2],sen[5]))
length = len(sen)
mid_char = length // 2
print('The mid character letter is:',sen[mid_char])
if length % 2 == 0:
    print("Adjoining letter for the even characters:",sen[mid_char-1]+sen[mid_char]+sen[mid_char+1])
else: 
    print("Adjoining letter for the odd characters:",sen[mid_char-1]+sen[mid_char]+sen[mid_char+1])
