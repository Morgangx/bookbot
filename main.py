from stats import get_book_text, get_number_of_words

def main() -> None:
    contents: str = get_book_text("books/frankenstein.txt")
    word_count: int = get_number_of_words(contents)
    print(f"Found {word_count} total words")

main()