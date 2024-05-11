# filename: main.py
from fastapi import FastAPI
from routers.orders_router import router as orders_router
from database import initialize_database, load_initial_data
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("Initializing the database and loading data...")
    initialize_database()
    load_initial_data()
    print("Database setup complete.")


# Mount the orders router
app.include_router(orders_router, prefix="/api/v1", tags=["orders"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
