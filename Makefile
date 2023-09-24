run:
	uvicorn credit_card.main:app --port 8000 --reload
db:
	@docker run --name postgres --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -p 5432:5432 -it postgres:14.1-alpine