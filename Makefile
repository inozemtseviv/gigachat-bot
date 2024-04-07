.PHONY: serve
serve:
	source venv/bin/activate && python main.py

.PHONY: up
up:
	docker-compose -f ./docker-compose.yml -p tg-gigachat up --build

.PHONY: down
down:
	docker-compose -f ./docker-compose.yml -p tg-gigachat down
