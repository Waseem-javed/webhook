from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.v1.api import api_router
from app.db.session import engine
from app.db.base import Base
from app.core.config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API for receiving and storing webhook events with signature verification.",
    openapi_url="/openapi.json"
)

# Root redirect to documentation
@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")

# Include API router
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)