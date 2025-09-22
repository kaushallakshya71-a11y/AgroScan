from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AgroScan Backend Running 🚀"}

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Backend healthy ✅"}