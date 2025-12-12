from __future__ import annotations
import sqlite3
from typing import Iterator, TYPE_CHECKING
from contextlib import contextmanager
from pathlib import Path

if TYPE_CHECKING:
    from src.quiz import Quiz, Question


class Database:
    def __init__(self):
        self.db_path = Path("assets/db/quiz.db")
        self._create_database()


    def _create_database(self):
        with self.get_connection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS QUIZ (
                    z_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS QUESTIONS (
                    q_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    z_id INTEGER NOT NULL REFERENCES QUIZ(z_id),
                    question TEXT UNIQUE NOT NULL,
                    type TEXT CHECK (type IN ('CHOICE', 'INPUT')) NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TYPE_CHOICE (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    q_id INTEGER NOT NULL REFERENCES QUESTIONs(q_id),
                    content TEXT NOT NULL,
                    correct INTEGER DEFAULT 0
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TYPE_INPUT (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    q_id INTEGER NOT NULL REFERENCES QUESTIONs(q_id),
                    expected TEXT NOT NULL
                )
            """)

    @contextmanager
    def get_connection(self) -> Iterator[sqlite3.Cursor]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception:
            import traceback
            traceback.print_exc()
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


    def add_quiz(self, quiz: Quiz):
        ...


    def add_question(self, z_id: int, question: Question):
        ...


    def load_quiz(self) -> Quiz:
        ...
