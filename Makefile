run:
	python main.py

seed:
	python app/database/seed/seed.py

migration:
	alembic upgrade head

test:
	pytest --pyargs tests

db_docs:
	dbdocs build doc/db.dbml

db_schema:
	dbml2sql --postgres -o doc/schema.sql doc/db.dbml