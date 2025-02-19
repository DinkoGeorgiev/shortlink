from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import FileResponse, RedirectResponse

from app.database import get_session
from app.models import LinkModel

# Kept separate, the webapp functionality can be easily moved to its dedicated service as necessary.
router = APIRouter(
    prefix="",
    tags=["web"],
)


@router.get("/", response_class=FileResponse)
async def read_index():
    """Serve the index html file

    :return: Response with html file
    """
    return FileResponse("static/index.html")


@router.get("/{link_id}")
async def redirect_link(link_id: str, db: AsyncSession = Depends(get_session)):
    """Endpoint to redirect to the mapped long url

    :param link_id: The link id
    :param db: Db session to use
    :return: The http redirect response
    :raises HTTPException if the specified link is not found
    """
    link = (await db.scalars(select(LinkModel).where(LinkModel.id == link_id))).first()

    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    response = RedirectResponse(url=link.long_link)
    return response
