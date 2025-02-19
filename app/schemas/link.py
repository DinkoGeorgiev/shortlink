from typing import Annotated, Optional
from urllib.parse import urlparse

from pydantic import AfterValidator, BaseModel, ConfigDict


def is_valid_link(value: str) -> str:
    """Validate the supplied link

    :param value: The value to check
    :return: Valid value
    :raise: ValueError if the link is invalid
    """
    parsed = urlparse(value)
    if parsed.scheme not in ["http", "https"]:
        raise ValueError(f"Invalid url scheme: {parsed.scheme}")
    return value


class LinkSchema(BaseModel):
    """Link schema validator"""

    model_config = ConfigDict(from_attributes=True)

    id: Optional[str] = ""
    long_link: Annotated[str, AfterValidator(is_valid_link)]


class ShortLinkSchema(LinkSchema):
    """Short link schema validator"""

    short_link: str
