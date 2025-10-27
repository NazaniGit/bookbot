def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return(text)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
main() 