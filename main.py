def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    word_number = word_count(text)
    print(f"Found {word_number} total words")
    
main()