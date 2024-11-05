from fastapi import APIRouter, HTTPException

from app.dtos.article_and_comments_response import ArticleAndCommentsResponse
from app.services.article_service import service_get_article_and_comments

router = APIRouter(prefix="/v1/articles", tags=["게시글"], redirect_slashes=False)


@router.get("/{article_id}", response_model=ArticleAndCommentsResponse)
async def router_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:

    # validation
    for stop_word in {"!", "#", "@", ":", ";"}:
        if stop_word in article_id:
            raise HTTPException(status_code=400, detail=f"특수 문자 불가")
    return await service_get_article_and_comments(article_id)
