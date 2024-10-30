from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Article(
    BaseModel, Model
):  # 다중 상속을 받음. BaseModel로부터 3개 컬럼을 상속 받음. 나머지는 Model로 부터
    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)

    # 본문
    body = fields.TextField()

    # 텍스트 필드는 길이 제한이 없다는 장점
    # but 인덱스에 넣을 수 없다는 단점
    # 인덱스는 메모리에 들어가는 밸런스 트리인데
    # 길이 제한이 없는 값을 많이 넣으면 메모리가 터짐

    class Meta:
        table = "articles"

    @classmethod
    async def get_one_by_id(cls, id: str) -> Article:
        # Artcle이 완벽히 정의돼있지않은 상태에서 Article을 다시 참조했으므로 에러가 난다
        # 이 문제를 해결하기 위해서는 from __futures__ import annotations 해준다
        return await cls.get(id=id)
