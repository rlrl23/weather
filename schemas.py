from __future__ import annotations

from pydantic import BaseModel


class RequestHistory(BaseModel):
    id: int
    user_ip: str
    city_name: str
    created_at: str
