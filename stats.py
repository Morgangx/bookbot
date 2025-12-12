from typing import TypedDict

class CharCount(TypedDict):
    char: str
    num: int

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents: str = f.read()
    return file_contents

def get_number_of_words(contents: str) -> int:
    words: list[str] = contents.split()
    return len(words)

def count_characters(contents: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}
    contents_l = contents.lower()
    for ch in contents_l:
        if ch not in char_dict:
            char_count: int = contents_l.count(ch)
            char_dict[ch] = char_count
    return char_dict

def get_characters(character_counts: dict[str, int]) -> list[CharCount]:
    list_of_characters: list[CharCount] = []
    for k in character_counts:
        list_of_characters.append({
            "char": k,
            "num": character_counts[k]
            })

    def sort_by_num(dictionary: CharCount) -> int:
        return dictionary["num"]

    list_of_characters.sort(reverse=True, key=sort_by_num)

    return list_of_characters