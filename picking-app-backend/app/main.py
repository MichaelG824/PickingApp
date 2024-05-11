# filename: main.py
from fastapi import FastAPI
from routers.orders_router import router as orders_router
from database import initialize_database, load_initial_data
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from humps import camelize
from starlette.responses import Response, JSONResponse, StreamingResponse  # Include StreamingResponse here

class CamelCaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Check if the response is a StreamingResponse or similar
        if isinstance(response, StreamingResponse):
            return response  # Do not attempt to modify StreamingResponse

        # Ensure response is JSON and has a body attribute
        if isinstance(response, JSONResponse):
            data = response.body.decode()  # Assuming body is a byte string
            modified_data = json.loads(data)  # Convert string to dictionary
            camelized_data = camelize(modified_data)  # Camelize keys
            response.body = json.dumps(camelized_data).encode('utf-8')  # Convert back to byte string
        return response

app = FastAPI()

app.add_middleware(CamelCaseMiddleware)

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
