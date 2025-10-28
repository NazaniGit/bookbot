from stats import word_count, char_count, char_sort
import sys 
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_number = word_count(text)
    chars = char_count(text)
    sorted_chars = char_sort(chars)
    
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {path_to_file}")
    
    print("----------- Word Count ----------")
    
    print(f"Found {word_number} total words")
    
    print("--------- Character Count -------")

    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()