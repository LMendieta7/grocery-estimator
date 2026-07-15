from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes.product import router as product_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Smart Grocery API",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(product_router, prefix="/api", tags=["products"])

    return app


app = create_app()


@app.get("/health")
def health_check():
    return {"status": "ok"}
