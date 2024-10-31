from app.dtos.article_and_comments_response import (ArticleAndCommentsResponse,
                                                    CommentResponse)
from app.models import comment
from app.models.article import Article
from app.models.comment import Comment


async def service_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:
    article = await Article.get_one_by_id(article_id)
    comments = await Comment.get_all_by_article(article_id)

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
