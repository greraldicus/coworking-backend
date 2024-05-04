from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"


class Settings(BaseModel):
    auth_jwt: AuthJWT = AuthJWT()
