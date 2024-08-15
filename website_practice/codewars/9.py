"""
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

"""


def shortcut(s):
    listo = []
    for item in range(len(s)):
        if s[item].islower() and s[item].lower() in ["a", "e", "i", "o", "u"]:
            pass
        else:
            listo.append(s[item])
    return "".join(listo)


print(shortcut("goodbye"))
print(shortcut("HELLO"))

"""
f shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
"""
