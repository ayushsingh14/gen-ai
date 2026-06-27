from __future__ import annotations

from pgvector_practice.db import create_schema, insert_document, vector_search


def main() -> None:
    create_schema()
    print("Created schema. You can now insert documents and run vector search.")
    sample_embedding = [0.1] * 1536
    insert_document("Sample document from CLI", sample_embedding)
    print("Inserted one sample document.")
    results = vector_search(sample_embedding, limit=3)
    print("Search results:")
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
