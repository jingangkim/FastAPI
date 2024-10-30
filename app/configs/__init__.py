from app.configs.base_settings import Settings


def get_settings() -> Settings:
    # 1. pydantic은 기본적으로 환경 변수에서 설정 값을 읽는다
    # 2. env_file을 전달한다면 .env를 읽는다.
    # env_file과 환경변수 중에서 항상 환경 변수가 우선시 된다
    # ex) 환경변수에 MY_NAME=진강, env_file에 MY_NAME이 마토 라면 환경변수가 우선순위라 MY_NAME은 진강
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )


settings = get_settings()