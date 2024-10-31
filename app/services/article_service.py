from app.dtos.article_and_comments_response import (ArticleAndCommentsResponse,
                                                    CommentResponse)
from app.models import comment
from app.models.article import Article
from app.models.comment import Comment


async def service_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:
    import asyncio

#asyncio.gather():란? 우선 parallel과 concurrent의 차이를 알 것
    # 해야할 일(task)이 3개인 경우
    # 사람 3명이 존재한다면 패러렐은 셋에게 각각 하나의 일을 시킴
    # 콘큐런트의 경우 사람 1명에게 효율적으로 일을 수행시킴
        # 이 경우, 무엇 하나가 지연되면 나머지도 지연이 됨.
    # 사람 = cpu core
    # task = io요청 (db호출, http호출 등)
    # 각각 하나의 일을 시킨 것 = IO요청을 받아들인 주체(데이터베이스, 외부서버)
    #gather는 concurrent하게 비동기 호출하는 것.
    #

    article, comments = await asyncio.gather(
        Article.get_one_by_id(article_id), Comment.get_all_by_article(article_id)
    )
    # 직렬
    # article = await Article.get_one_by_id(article_id)
    # comments = await Comment.get_all_by_article(article_id)

    return ArticleAndCommentsResponse(
        id=article.id,
        author=article.author,
        title=article.title,
        body=article.body,
        comments=tuple(
            CommentResponse(id=comment.id, author=comment.author, body=comment.content)
            for comment in comments
        ),
    )
