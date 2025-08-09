import requests
from fastapi import HTTPException

AUDIO_BASE_URL = "https://everyayah.com/data/AbdulSamad_64kbps_QuranExplorer.Com/{surah}{ayah}.mp3"

def zero_pad3(n: int) -> str:
    return str(n).zfill(3)

def download_verse_audio(surah: int, ayah: int) -> bytes:
    surah_str = zero_pad3(surah)
    ayah_str = zero_pad3(ayah)
    url = AUDIO_BASE_URL.format(surah=surah_str, ayah=ayah_str)

    try:
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Audio not found.")
        return response.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch audio: {str(e)}")
