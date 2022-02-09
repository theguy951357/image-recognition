from dataclasses import dataclass
from enum import Enum


@dataclass
class Config:
    image: str
    model: str
    name: str
    out: str
    train: str
    epochs: int
