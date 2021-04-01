string = list(input())
vowels = list("aeiou")
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def is_letter(i):
    for letter in alphabet:
        if i == letter:
            return True
        else:
            continue
    else:
        return False

def is_vowel(i):
    for vowel in vowels:
        if i == vowel:
            print("vowel")
            break
        else:
            continue
    else:
        print("consonant")

for char in string:
    if is_letter(char):
        is_vowel(char)
    else:
        break