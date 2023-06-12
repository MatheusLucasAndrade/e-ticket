from app.api.v1.api_routes import api_router
from fastapi import FastAPI
import uvicorn

app = FastAPI(
     title="ETICKET - Controle de clients",
     openapi_url="/v1",
     root_path= ""
)

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)