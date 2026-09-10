from fastapi import FastAPI


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