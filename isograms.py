def is_isogram(string):
    string = string.lower()
    characters = []
    for ch in string:
        if ch in characters:
            return False
        characters.append(ch)
    return True
