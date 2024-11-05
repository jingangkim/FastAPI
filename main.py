from fastapi import FastAPI

from app.configs.database_settings import initialize
from app.routers.article_router import router as article_router
from app.routers.health_router import router as health_router

app = FastAPI()
app.include_router(article_router)
app.include_router(health_router)
initialize(app)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
