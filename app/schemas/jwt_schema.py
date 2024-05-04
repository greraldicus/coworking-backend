from .base_schema import BaseModel


class JwtTokenSchema(BaseModel):
    token: str
    token_type: str


class JwtPayloadSchema(BaseModel):
    sub: int
    username: str
    iat: str
    exp: str
