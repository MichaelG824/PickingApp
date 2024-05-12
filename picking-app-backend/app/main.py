from fastapi import FastAPI
from routers.pick_router import router as pick_router
from db.database import initialize_database, load_initial_data
from fastapi.middleware.cors import CORSMiddleware

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
