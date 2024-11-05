import asyncio

from httpx import AsyncClient
from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.models.comment import Comment
from main import app


class TestArticleRouter(TestCase):
    async def test_get_article_and_comment(self) -> None:
        article_id = "Test_article"
        article = await Article.create(
            id=article_id, author="author", title="title", body="body"
        )

        await asyncio.gather(
            Comment.create(
                id="comment1", article=article, author="c1_author", content="c1_content"
            ),
            Comment.create(
                id="comment2", article=article, author="c2_author", content="c2_content"
            ),
        )
        # when절
        # 기존에 동기 방식으로 http요청을 할 때는 requests를 썼다
        # 비동기 방식으로 httpx 요청을 하고 싶다면 httpx를 쓴다
        # router테스트는 url을 거쳐서 실제로 api를 호출하는 테스트다.

        # httpx.AsycCliant(app=app) async client에 app을 전달하면
        # asgi app에 바로 요청할 수 있는 clientrk todtjdehla
        async with AsyncClient(app=app, base_url="http://test") as ac:
            # app을 전달해서 AsycClient를 만들었기 때문에
            # url의 scheme나 host를 전달할 필요 없이 바로 경로만 적으면 된다
            response = await ac.get(
                url=f"/v1/articles/{article_id}",
                headers={"Accept": "application/json"},
            )

        # then
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertEqual(response_body["id"], article_id)
        self.assertEqual(response_body["author"], "author")
        self.assertEqual(response_body["title"], "title")
        self.assertEqual(response_body["body"], "body")

        self.assertEqual(len(response_body["comments"]), 2)
        self.assertEqual(response_body["comments"][0]["id"], "comment1")
        self.assertEqual(response_body["comments"][0]["author"], "c1_author")
        self.assertEqual(response_body["comments"][0]["body"], "c1_content")

        self.assertEqual(response_body["comments"][1]["id"], "comment2")
        self.assertEqual(response_body["comments"][1]["author"], "c2_author")
        self.assertEqual(response_body["comments"][1]["body"], "c2_content")

        # 순서와 상관 없이 검증하는 방법은 순서가 없는 자료형 set()을 활용한다.
        id_set = {comment["id"] for comment in response_body["comments"]}
        self.assertIn("comment1", id_set)
        self.assertIn("comment2", id_set)

        # 방법2 dict를 사용하는 방법이 있다
        comment_dict = {comment["id"]: comment for comment in response_body["comments"]}
        result_comment1 = comment_dict["comment1"]
        self.assertEqual(result_comment1["author"], "c1_author")
        self.assertEqual(result_comment1["body"], "c1_content")

        result_comment2 = comment_dict["comment2"]
        self.assertEqual(result_comment2["author"], "c2_author")
        self.assertEqual(result_comment2["body"], "c2_content")
