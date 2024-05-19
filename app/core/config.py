from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_minutes: int = 43200


class Settings(BaseModel):
    auth_jwt: AuthJWT = AuthJWT()
    static_dir: Path = BASE_DIR.joinpath("static")


settings = Settings()
