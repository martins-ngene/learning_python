# Creating an ASCII translator
# Put in a word, it translates to its ASCII value

def to_ascii_translator(word):

    alphabets_ascii = {
        "A": "65",
        "B": "66",
        "C": "67",
        "D": "68",
        "E": "69",
        "F": "70",
        "G": "71",
        "H": "72",
        "I": "73",
        "J": "74",
        "K": "75",
        "L": "76",
        "M": "77",
        "N": "78",
        "O": "79",
        "P": "80",
        "Q": "81",
        "R": "82",
        "S": "83",
        "T": "84",
        "U": "85",
        "V": "86",
        "W": "87",
        "X": "88",
        "Y": "89",
        "Z": "90",
        " ": " ",
    }

    translated = ""

    is_letter = True

    for alphabet in word:
        for letter in alphabets_ascii:
            if alphabet.upper() in letter:
                if alphabet.upper() == letter:
                    alphabet = alphabets_ascii.get(letter)
                    translated = translated + alphabet
            if not is_letter:
                print("Enter a word")

    return translated


print(to_ascii_translator(input("Enter a word: ")))

'''
I need to refactor the above function to check if the word is not an alphabet.
'''
