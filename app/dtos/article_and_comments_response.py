from pydantic import BaseModel


class CommentResponse(
    BaseModel
):  # response dto를 생성한다. 결과 안에 무엇을 넣은 것이냐?
    id: str  # 댓글이 가진 컬럼 중 아래 3가지 컬럼을 클라이언트에게 전달할 것임.
    author: str
    body: str


# fastapi에서 dto는 pydantic에 basemodel을 상속받음


class ArticleAndCommentsResponse(BaseModel):  # 게시글 + 댓글을 모두 담는 dto 생성
    id: str
    author: str
    title: str
    body: str
    comments: tuple[CommentResponse, ...]
    # list대신 tuple을 사용했음
    # list는 '길이'(요소)가 가변성이다.  ex)리스트에 요소를 추가, 삭제.append() , .insert(), .pop() 하는 경우엔 길이가 변함
    # tuple은 type annotation이 '길이'도 지정한다
    # 길이를 모르는 경우 ', ...'을 사용함
    # 왜 튜플을 사용했는지? -> 튜플은 immutable(불변) -> 예측이 쉽다 -> 더 잘 읽힌다
