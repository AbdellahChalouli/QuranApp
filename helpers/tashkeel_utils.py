import mishkal.tashkeel

def apply_diacritics(text: str) -> str:
    vocalizer = mishkal.tashkeel.TashkeelClass()
    return vocalizer.tashkeel(text)
