test = ["alliteration", "appeals", "to", "almost", "anyone", "in", "the", "room"]

def print_upper_words(sentence, startswith):
    for word in sentence:
        for letter in startswith:
            if word.startswith(letter):
                print(word.upper())
                break

    
    
print_upper_words(test,["a", "t"]);