from .base_schema import BaseSchema


class FileInfoSchema(BaseSchema):
    filename: str
    filesize: int
    content_type: str
    download_url: str
