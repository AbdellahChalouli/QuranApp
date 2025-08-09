from fastapi import APIRouter, UploadFile, File
from services.analyze_service import analyze_audio

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analyze_audio(file)
    return result
