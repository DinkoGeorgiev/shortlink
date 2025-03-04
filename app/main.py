import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.logging_utils import setup_logging
from app.routers.link import router as link_router
from app.routers.web import router as web_router

setup_logging()


app = FastAPI(title="Short Link", docs_url="/api/docs", redoc_url="/api/redoc")

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(link_router)
app.include_router(web_router)
