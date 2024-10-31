from fastapi import APIRouter

from app.dtos.article_and_comments_response import ArticleAndCommentsResponse
from app.services.article_service import service_get_article_and_comments

router = APIRouter(prefix='/v1/articles', tags=['articles'], redirect_slashes=False)

@routers.get("/{article_id}", response_model=ArticleAndCommentsResponse)
async def get_article_and_comments(article_id: int) -> ArticleAndCommentsResponse:
    return await service_get_article_and_comments