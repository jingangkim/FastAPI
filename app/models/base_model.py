from tortoise import fields


class BaseModel:  # 앞으로 모든 모델들이 BaseModel을 상속받겠다
    # 멤버 변수와 메소드를 물려받지만
    # basemodel엔 메소드는 없고 멤버변수(id, created_at, modified_at)만 있다

    # audit
    # create_at modified_at은 audit(누가, 언제, 무엇을, 어떻게 수정?) 컬럼이라고 한다

    id = fields.CharField(primary_key=True, max_length=40)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
