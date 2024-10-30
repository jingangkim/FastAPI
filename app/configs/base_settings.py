from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    # enum을 만드는 이유 : 자동완성, 타입체킹
    # LOCAl처럼 대소문자 실수 했을 때 IDE가 잡아줌
    LOCAL = "local"  # 내가 개발하는 컴퓨터
    STAGE = "stage"  # QA와 함께 정상 동작 확인하는 곳. 테스트
    PROD = "prod"  # 프로덕션 : 실제 배포 되는 곳


class Settings(BaseSettings):  # 지금 내 환경을 설정
    ENV: Env = Env.LOCAL  # 내 환경은 로컬
    DB_HOST: str = "localhost"  # 127.0.0.1과 같은 의미임
    DB_PORT: int = 3306
    DB_USER: str = "root"  # mysql의 루트(기본)계정
    DB_PASSWORD: str = "1234"
    DB_DB: str = "oz_fastapi5"
