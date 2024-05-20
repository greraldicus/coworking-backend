from os import path

from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends
from starlette.responses import FileResponse

from app.core import settings
from app.dependencies import get_user_role_by_token_payload
from app.auth import ROLE_ADMIN
from app.dal import upload_file
from app.schemas import FileInfoSchema

files_router = APIRouter(prefix="/files")


@files_router.post(
    path="/upload",
    response_model=FileInfoSchema
)
async def upload_file_endpoint(
    file: UploadFile = File(...),
    role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="forbidden"
        )
    return await upload_file(file)


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
