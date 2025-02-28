from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from . import templates

router = APIRouter(
    tags=["index", "views"],
    responses={
        404: {
            "description": "Not found",
        }
    },
)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
