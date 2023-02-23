"""
Byron Wallace + Ben Rye
DS2k lecture 7 notes

Writing Functions
"""

# simplified code block
def get_letter_pronunciation(char, letters, pronounce_letters):
    for letter_idx in range(len(letters)):
        letter = letters[letter_idx]
        if char.lower() == letter.lower():
            cur_letter_pronunciation = pronounce_letters[letter_idx]
            break
    return cur_letter_pronunciation


# Let's write a function that accepts a tiny string
# And returns a "phonetic" pronunciation
def pronounce():
    str_to_pronounce = "hello world"

    with open("pronunciation.txt", 'r') as infile:
        letters = infile.readline().split(' ')
        letters.pop(0)  # 'Letters'

        pronounce_letters = infile.readline().split(' ')
        pronounce_letters.pop(0)  # 'Pronunciation'


    # char may be temp var in for loop, but we still need to init the other ones
    pronunciation = ""
    for char in str_to_pronounce:
        cur_letter_pronunciation = get_letter_pronunciation(char,
                                                            letters,
                                                            pronounce_letters)
        pronunciation += '-' + cur_letter_pronunciation
        # loop up to pronounce letter 'char'
        # find its ___ to char
    # Ok we're all 
    print(pronunciation)


pronounce()
