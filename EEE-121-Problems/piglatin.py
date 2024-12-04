def piglatin_translate(phrase):
    """Translates a phrase into Pig Latin."""
    vowels = ["a", "e", "i", "o", "u"]
    pig_latin = ""
    for word in phrase.split():
        if word[0] in vowels: # if word starts with a vowel
            pig_latin += word + "way "
        elif word[0] not in vowels:
            if word[1] in vowels:
                pig_latin += word[1:] + word[0] + "ay "
            elif word[1] not in vowels:
                pig_latin += word[2:] + word[0:2] + "ay "
    return pig_latin

        

if __name__ == "__main__":
    input_line = str(input())
    print(piglatin_translate(input_line))
