from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.article import Article
from app.models.base_model import BaseModel


class Comment(BaseModel, Model):
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        "models.Article", related_name="comments", db_constraint=False
    )
    author = fields.CharField(max_length=255)
    content = fields.TextField()
    # 필드 폴인키릴레이션[아티클]은 타입
    # 필드 폴인키 필드(...)는 실제 값임
    # 실제 db에 들어가는 것은 'article_id'
    #

    class Meta:
        table = "comments"

    @classmethod
    async def get_all_by_article(cls, article: str) -> list[Comment]:
        return await cls.filter(article=article).all()

    # filter().all()을 보면 알 수 있지만
    # tortoise orm은 처음 설계 의도가 django orm과 흡사하다
    # django에 있던 것들이 앵간하면 tortoise orm에도 다 있다
