import uuid
from datetime import datetime
from os import path

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from starlette.responses import FileResponse

from app.core import settings

files_router = APIRouter(prefix="/files")


@files_router.post(
    path="/upload"
)
async def upload_file(
    file: UploadFile = File(...)
):
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{now}_{uuid.uuid4().hex[:8]}_{file.filename}"
    file_path = path.join(settings.static_dir, unique_filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {
        "filename": unique_filename,
        "file_size": path.getsize(file_path),
        "content_type": file.content_type,
        "download_url": f"/download/{unique_filename}"
    }


@files_router.get("/download/{filename}")
async def download_file(
        filename: str
):
    file_path = path.join(settings.static_dir, filename)
    if not path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )

    return FileResponse(file_path)
