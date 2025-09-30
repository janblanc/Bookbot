def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    text = text.lower()
    characters_count = {}
    for character in text:
        if character not in characters_count:
            characters_count[character] = 1
        else:
            characters_count[character] += 1
    return characters_count

def sort_on(char):
    return char["num"]

def separate_dict(num_characters):
    newdicts = []
    for ch, n in num_characters.items():
        newdicts.append({"char": ch, "num": n})
    newdicts.sort(reverse=True, key=sort_on)
    return newdicts

