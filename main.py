from fastapi import FastAPI
from routes import analyze_router, audio_router, compare_router

app = FastAPI()

app.include_router(analyze_router.router, prefix="/api")
app.include_router(audio_router.router, prefix="/api")
app.include_router(compare_router.router, prefix="/api")
