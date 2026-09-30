from fastapi import FastAPI

app = FastAPI(
    title="AI Video Studio API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Video Studio API is running",
        "version": "0.1.0"
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }