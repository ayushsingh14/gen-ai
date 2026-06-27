from pgvector_practice.db import create_schema


def test_create_schema_executes_without_error():
    create_schema()
