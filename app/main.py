from fastapi import FastAPI
from desk_booking.router import router as desk_router


app = FastAPI()
app.include_router(desk_router)


@app.get("/")
async def root():
    return {"message": "Hello API"}
