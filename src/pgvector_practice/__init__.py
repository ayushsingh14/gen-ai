"""pgvector practice package."""

from .db import create_schema, insert_document, vector_search

__all__ = ["create_schema", "insert_document", "vector_search"]
