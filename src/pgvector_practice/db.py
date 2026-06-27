import os
from typing import List, Optional

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pgvector_user:secret@localhost:5432/pgvector_db",
)


def get_connection():
    conn = psycopg.connect(DATABASE_URL)
    register_vector(conn)
    return conn


def create_schema():
    with get_connection() as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                embedding VECTOR(1536)
            );
            """
        )


def insert_document(content: str, embedding: List[float]):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO documents (content, embedding) VALUES (%s, %s);",
            (content, embedding),
        )


def vector_search(query_embedding: List[float], limit: int = 5) -> List[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, content, embedding <-> %s AS distance FROM documents ORDER BY distance LIMIT %s;",
            (query_embedding, limit),
        )
        return [dict(row) for row in rows]
