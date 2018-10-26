text = 'We are having a great time in polisinos. there are very smart students here'

count_vowels = 0
count_consonats = 0

for letter in text:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
         count_vowels += 1
    elif letras not in [' ','.']:   
         count_consonats = count_consonats + 1
    print('Number of vowels in text is: ' + str(count_vowels))
    print('Number of vowels in text is: ' + str(count_consonants))