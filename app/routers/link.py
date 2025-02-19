from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.link import LinkModel
from app.schemas.link import LinkSchema, ShortLinkSchema
from app.utils import generate_random_string

router = APIRouter(
    prefix="/api/link",
    tags=["link"],
)


@router.post("/", response_model=ShortLinkSchema)
async def create_link(link: LinkSchema, request: Request, db: AsyncSession = Depends(get_session)):
    """Create link endpoint

    :param link: Link schema object
    :param request: The request object
    :param db: Database session
    :return: The ShortLink schema object representing the created link record
    :raises HTTPException on invalid data supplied
    """
    if link.long_link.startswith(str(request.base_url)):
        raise HTTPException(status_code=400, detail="Already a short link.")

    requested_link_id = link.id
    if not link.id:
        link.id = generate_random_string(5)

    for link_size in [5, 6, 7, 8]:
        link_model = LinkModel(**link.model_dump())
        db.add(link_model)
        try:
            await db.commit()
        except IntegrityError as exc:
            if requested_link_id:
                raise HTTPException(status_code=409, detail="Link already exists") from exc
            await db.rollback()
            # Try generating another id
            link.id = generate_random_string(link_size)
        else:
            short_link = ShortLinkSchema(short_link=f"{request.base_url}{link.id}", **link.model_dump())
            return short_link
    # Give up
    raise HTTPException(status_code=422, detail="Unable to create link at this time, please try again later.")


@router.get("/{link_id}", response_model=LinkSchema)
async def get_link(link_id: str, db: AsyncSession = Depends(get_session)):
    """An endpoint to get link information based on its id, without causing a redirect

    :param link_id: Link id
    :param db: Database session
    :return: Link information
    :raises HTTPException if link not found
    """
    link = (await db.scalars(select(LinkModel).where(LinkModel.id == link_id))).first()

    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link
