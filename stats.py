def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents: str = f.read()
    return file_contents

def get_number_of_words(contents: str) -> int:
    words: list[str] = contents.split()
    return len(words)
