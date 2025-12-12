from typing import TypedDict, Literal
from src.quiz.database import Database


class Question(TypedDict):
    Type: Literal['CHOICE', 'INPUT']
    question: str
    answer: str
    choices: list[str]


class Quiz(TypedDict):
    name: str
    questions: list[Question]


class VARS:
    DATABASE: Database


def init():
    VARS.DATABASE = Database()


def load(name: str):
    ...