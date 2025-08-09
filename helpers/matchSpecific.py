from difflib import SequenceMatcher

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.strip(), b.strip()).ratio()

def compare_with_verse(transcribed_text: str, verse_text: str) -> float:
    return similarity(transcribed_text, verse_text)
