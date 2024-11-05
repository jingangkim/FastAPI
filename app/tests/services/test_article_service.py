from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.services.article_service import service_get_article_and_comments


class TestArticleService(TestCase):
    async def test_get_article_and_comments(self) -> None:
        # 뭘 가지고
        # 단순 함수(plain function). 호출하는 것만으로 테스트가 가능하다. 하지만 router테스트는 ?
        article_id = "test_article"
        article = await Article.create(
            id=article_id, author="author", title="title", body="body"
        )
        # 뭘 할건데
        article_and_comment = await service_get_article_and_comments(article_id)
        # 이런 결과가 맞는지
        self.assertEqual(article_and_comment.id, article_id)
        self.assertEqual(article_and_comment.author, "author")
        self.assertEqual(article_and_comment.title, "title")
        self.assertEqual(article_and_comment.body, "body")
