# gen-ai

Practice repo for PostgreSQL `pgvector` experiments.

## Structure

- `docker-compose.yml` — PostgreSQL with pgvector ready to run
- `sql/schema.sql` — schema for `documents` with a `VECTOR(1536)` column
- `sql/sample_data.sql` — sample insert statements
- `src/pgvector_practice/` — Python helpers for schema, insert, and search
- `tests/test_db.py` — simple DB smoke test
- `.env.example` — example environment variables
- `notebooks/` — place for Jupyter notebooks

## Setup

1. Copy `.env.example` to `.env`
2. Start the database:
   ```bash
   docker compose up -d
   ```
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run the CLI to create schema and insert a sample row:
   ```bash
   python -m pgvector_practice.cli
   ```

## Notes

- Use `DATABASE_URL` to point your local or hosted PostgreSQL instance.
- `pgvector` requires the `vector` extension and a compatible PostgreSQL build.
- The `ankane/pgvector` Docker image includes the extension out of the box.
