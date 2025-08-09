from pymongo import MongoClient

def get_all_verses():
    client = MongoClient("mongodb://localhost:27017/")
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
    client = MongoClient("mongodb://localhost:27017/")
    db = client["QURAN"]
    collection = db["quran"]

    doc = collection.find_one({ "number": surah_number })
    if not doc:
        return None

    for verse in doc.get("verses", []):
        if verse.get("number") == ayah_number:
            return {
                "text": verse.get("text", {}).get("ar", "")
            }

    return None
