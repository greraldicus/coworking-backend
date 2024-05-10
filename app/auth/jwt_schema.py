from app.schemas.base_schema import BaseModel


class JwtSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class JwtPayloadSchema(BaseModel):
    sub: int
    username: str
