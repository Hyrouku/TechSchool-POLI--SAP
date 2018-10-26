def count_vowels(text):
    count_vowels = 0

    for letter in text:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count_vowels += 1

    print('The number of vowels is ' + str(count_vowels))

    vowels = input('Insert a phrase: ')
    count_vowels(vowels)