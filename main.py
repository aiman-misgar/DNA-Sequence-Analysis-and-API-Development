
from fastapi import FastAPI
from app.routes import router  # import your router

app = FastAPI(
    title="Ancient DNA Sequence Analysis API",
    description="API to analyze and compare DNA sequences from ancient remains.",
   
)

app.include_router(router)

# Optional root
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ancient DNA API!"}  

