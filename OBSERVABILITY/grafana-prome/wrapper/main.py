from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

def check_auth(request: Request):
    auth = request.headers.get("authorization")
    if not auth:
        raise HTTPException(status_code=401, detail="Authorization header required")
    print("✅ Authorization:", auth)


@app.post("/v1/traces")
async def traces(request: Request):
    check_auth(request)
    body = await request.body()
    print("📦 TRACES payload size:", len(body))
    return {"status": "ok"}


@app.post("/v1/metrics")
async def metrics(request: Request):
    check_auth(request)
    body = await request.body()
    print("📊 METRICS payload size:", len(body))
    return {"status": "ok"}


@app.post("/v1/logs")
async def logs(request: Request):
    check_auth(request)
    body = await request.body()
    print("🪵 LOGS payload size:", len(body))
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "wrapper running"}

