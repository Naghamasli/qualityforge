from fastapi import FastAPI
from app.routers.products import router as products_router


app = FastAPI(
    title="ShopForge Core API",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "core-api"
    }


app.include_router(products_router)