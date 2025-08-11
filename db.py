import os
from pymongo import MongoClient

# Read connection string from environment variable (safer than hardcoding)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://abdellah:Caw8RouI3pR7hkJf@cluster0.fkhd8hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

def get_all_verses():
    client = MongoClient(MONGO_URI)
    db = client["QURAN"]
    collection = db["quran"]
    all_verses = []
    for doc in collection.find():
        for verse in doc.get("verses", []):
            verse_text = verse.get("text", {}).get("ar", "")
            if verse_text:
                all_verses.append({
                    "text": verse_text,
                    "number": verse.get("number"),
                    "surah_number": doc.get("number"),
                    "surah_name": doc.get("name", {}).get("ar", "")
                })
    client.close()
    return all_verses


def get_verse_by_surah_and_ayah(surah_number: int, ayah_number: int) -> dict | None:
    client = MongoClient(MONGO_URI)
    db = client["QURAN"]
    collection = db["quran"]

    doc = collection.find_one({ "number": surah_number })
    if not doc:
        client.close()
        return None

    for verse in doc.get("verses", []):
        if verse.get("number") == ayah_number:
            client.close()
            return {
                "text": verse.get("text", {}).get("ar", "")
            }

    client.close()
    return None
