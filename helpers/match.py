from difflib import SequenceMatcher

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.strip(), b.strip()).ratio()

def find_best_match(transcribed_text: str, verses: list) -> tuple:
    best_match = None
    best_score = 0.0
    for verse in verses:
        score = similarity(transcribed_text, verse["text"])
        if score > best_score:
            best_score = score
            best_match = verse
    return best_match, best_score
