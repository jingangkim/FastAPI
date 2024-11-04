from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["살려주세요"])


class OkResponse(BaseModel):
    ok: bool
    extra_msg: str | None = None


@router.post("", response_model=OkResponse)
async def health() -> OkResponse:
    return OkResponse(ok=True)
