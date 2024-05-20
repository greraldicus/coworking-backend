from os import path
from datetime import datetime
import uuid

from fastapi import UploadFile, HTTPException, status

from app.schemas import FileInfoSchema
from app.core import settings


async def upload_file(
    file: UploadFile,
) -> FileInfoSchema:
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
    return FileInfoSchema(
        filename=unique_filename,
        filesize=path.getsize(file_path),
        content_type=file.content_type,
        download_url=f"/files/download/{unique_filename}"
    )
