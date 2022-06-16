run:
	python main.py

seed:
	python app/database/seed/seed.py

migration:
	alembic upgrade head