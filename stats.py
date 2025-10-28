def word_count(text):
    words = text.split()
    return len(words)
def char_count(text):
    chars = {}
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
def char_sort(chars):
    return sorted(chars.items(), key=lambda item: item[1], reverse=True)