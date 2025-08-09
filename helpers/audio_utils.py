import shutil
import os
from fastapi import UploadFile

UPLOAD_PATH = "uploaded_audio"

os.makedirs(UPLOAD_PATH, exist_ok=True)

def save_upload_file(file: UploadFile) -> str:
    path = os.path.join(UPLOAD_PATH, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return path
