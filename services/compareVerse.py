import whisper
from db import get_verse_by_surah_and_ayah
from helpers.tashkeel_utils import apply_diacritics
from helpers.audio_utils import save_upload_file
from helpers.matchSpecific import compare_with_verse

model = whisper.load_model("large") 

def compare_audio(file, surah:int , ayah:int) -> dict:
    path = save_upload_file(file)
    result = model.transcribe(path, language="ar")
    raw_text = result["text"]
    vocalized = apply_diacritics(raw_text)
    verseResult = get_verse_by_surah_and_ayah(surah,ayah)
    verse = verseResult["text"]
    score = compare_with_verse(vocalized, verse)
    
    return {
        "transcribed_text": vocalized,
        "match_score": round(score, 4),
        "verse": verse
    }
