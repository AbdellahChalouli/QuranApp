from fastapi import APIRouter, UploadFile, File, Query, HTTPException
from services.compareVerse import compare_audio

router = APIRouter()

@router.post("/compare")
async def compare_recitation(
    file: UploadFile = File(...),
    surah: int = Query(..., ge=1, le=114),
    ayah: int = Query(..., ge=1)
):
    try:
        result = compare_audio(file, surah, ayah)
        if not result["verse"]:
            raise HTTPException(status_code=404, detail="Verse not found in the database.")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
