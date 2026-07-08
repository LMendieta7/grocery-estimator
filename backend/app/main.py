from fastapi import FastAPI
from backend.app.api.routes.estimates import router as estimates_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Grocery Estimator API",
        version="0.1.0",
    )

    app.include_router(estimates_router, prefix="/api", tags=["estimates"])

    return app


app = create_app()


@app.get("/health")
def health_check():
    return {"status": "ok"}
