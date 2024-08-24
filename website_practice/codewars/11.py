"""
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


"""


def pig_it(text):
    text_listed = text.split(" ")
    for i in range(len(text_listed)):
        first_letter = text_listed[i][0]
        text_listed[i] + first_letter
    return text_listed


print(pig_it("Pig latin is cool"))
