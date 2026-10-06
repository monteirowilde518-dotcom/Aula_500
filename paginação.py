from math import ceil
  
from fastapi import Request
from pydantic import BaseModel


class Pagina[T](BaseModel):
    items: list[T]
    total: int
    page: int
    size: int
    pages: int
