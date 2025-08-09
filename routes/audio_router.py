from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from helpers.audio_downloader import download_verse_audio
from io import BytesIO

router = APIRouter()

@router.get("/verse-audio")
def get_verse_audio(
    surah: int = Query(..., ge=1, le=114),
    ayah: int = Query(..., ge=1)
):
    audio_bytes = download_verse_audio(surah, ayah)
    return StreamingResponse(BytesIO(audio_bytes), media_type="audio/mpeg")
