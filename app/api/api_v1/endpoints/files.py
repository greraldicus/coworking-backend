import uuid
from datetime import datetime
from os import path

from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends
from starlette.responses import FileResponse

from app.core import settings
from app.dependencies import get_user_role_by_token_payload
from app.auth import ROLE_USER, ROLE_ADMIN

files_router = APIRouter(prefix="/files")


@files_router.post(
    path="/upload"
)
async def upload_file(
    file: UploadFile = File(...),
    role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="forbidden"
        )
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{now}_{uuid.uuid4().hex[:8]}_{file.filename}"
    file_path = path.join(settings.static_dir, unique_filename)

    if file.content_type not in ["image/jpeg", "image/png", "image/svg+xml"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only jpeg, png, svg allowed"
        )
    if file.size > 2097152:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="allowed size less than 2MB"
        )

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
    filename: str,
    role: str = Depends(get_user_role_by_token_payload)
):
    if role not in [ROLE_USER, ROLE_ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="forbidden"
        )
    file_path = path.join(settings.static_dir, filename)
    if not path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )

    return FileResponse(file_path)
