from fastapi import APIRouter, HTTPException, status, Depends
from schemes import Message, MessageCreate
import crud.message as crud
from models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[Message])
async def get_messages(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud.get_messages(session=session)


@router.post("/", response_model=Message)
async def create_message(
    message_in: MessageCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud.create_message(session=session, message_in=message_in)


@router.get("/{message_id}", response_model=Message)
async def get_message(
    message_id: int, session: AsyncSession = Depends(db_helper.session_getter)
):
    message = await crud.get_message(session=session, message_id=message_id)
    if message:
        return message

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Message {message_id} not found!",
    )
