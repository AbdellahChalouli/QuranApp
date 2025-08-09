import whisper
from db import get_all_verses
from helpers.tashkeel_utils import apply_diacritics
from helpers.audio_utils import save_upload_file
from helpers.match import find_best_match

model = whisper.load_model("large")  # Load once globally

def analyze_audio(file) -> dict:
    path = save_upload_file(file)
    result = model.transcribe(path, language="ar")
    raw_text = result["text"]
    vocalized = apply_diacritics(raw_text)
    verses = get_all_verses()
    best_match, score = find_best_match(vocalized, verses)
    
    return {
        "transcribed_text": vocalized,
        "match_score": round(score, 4),
        "matched_verse": best_match
        
    }
