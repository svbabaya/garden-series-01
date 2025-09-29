from pydantic import BaseModel, ConfigDict
from models import Mode


class MessageBase(BaseModel):
    text: str
    caption: str
    mode: Mode
    is_displayed: bool = False


class MessageCreate(MessageBase):  # scheme for create
    pass


class Message(MessageBase):  # scheme for get response
    model_config = ConfigDict(from_attributes=True)
    id: int
