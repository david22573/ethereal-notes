from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from . import templates

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard", "views"],
    responses={
        404: {
            "description": "Not found",
        }
    },
)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data = {}
    return templates.TemplateResponse(
        "dashboard/index.html", {"request": request, "data": data}
    )
