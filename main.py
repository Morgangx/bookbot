from stats import get_book_text, get_number_of_words, count_characters, get_characters, CharCount
import sys


def main() -> None:
    print(sys.argv)
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path: str = sys.argv[1]
    
    contents: str = get_book_text(book_path)
    word_count: int = get_number_of_words(contents)
    char_dict: dict[str, int] = count_characters(contents)
    sorted_chars: list[CharCount] = get_characters(char_dict)

    characters_listings: str = ""
    for char_count in sorted_chars:
        if char_count["char"].isalpha():
            characters_listings += f"{char_count['char']}: {char_count['num']}\n"

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(characters_listings, end="")
    print("============= END ===============")
    
main()