from fastapi import FastAPI
from routers.pick_router import router as pick_router
from database import initialize_database, load_initial_data
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from humps import camelize
from starlette.responses import Response, JSONResponse, StreamingResponse
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await initialize_database()
    await load_initial_data()

app.include_router(pick_router, prefix="/api/v1/picks", tags=["pick"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
