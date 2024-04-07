.PHONY: serve
serve:
	uvicorn main:app --host localhost --port 3000

.PHONY: up
up:
	docker-compose -f ./docker-compose.yml -p tg-gigachat up --build

.PHONY: down
down:
	docker-compose -f ./docker-compose.yml -p tg-gigachat down
