<<<<<<< HEAD
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

=======
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

>>>>>>> 9d01fc8f0ff8f2102c69f574c24b4799c81fd56d
       