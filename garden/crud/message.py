from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import Message
from schemes import MessageCreate
from core.config import settings


async def get_messages(session: AsyncSession) -> list[Message]:
    sel = select(Message).order_by(Message.id)
    result: Result = await session.execute(sel)
    products = result.scalars().all()
    return list(products)


async def get_message_by_id(session: AsyncSession, message_id: int) -> Message | None:
    return await session.get(Message, message_id)


async def get_current_message(session: AsyncSession) -> Message | None:
    if session is None:
        return Message(
            text=settings.default_strings.message_text,
            author=settings.default_strings.message_author,
        )
    else:
        message_id = 1 # ToDo random select from ORDINARY messages
        return await session.get(Message, message_id)


async def create_message(session: AsyncSession, message_in: MessageCreate) -> Message:
    message = Message(**message_in.model_dump())
    session.add(message)
    await session.commit()
    # await session.refresh(message)
    return message
