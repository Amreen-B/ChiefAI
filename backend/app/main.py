from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.upload import router as upload_router
from app.api.analyse import router as analyse_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.history import router as history_router
from app.api.compare import router as compare_router


load_dotenv()

app = FastAPI(
    title="AgentBoard AI"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(upload_router)
app.include_router(analyse_router)
app.include_router(history_router)
app.include_router(compare_router)

@app.get("/")
def root():
    return{
        "message": "AgentBoard AI is running!"
    }