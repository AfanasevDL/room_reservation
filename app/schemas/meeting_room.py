from typing import Optional

from pydantic import BaseModel, Field


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.


class MeetingRoomDB(MeetingRoomCreate):
    id: int 