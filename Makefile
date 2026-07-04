dev:
	docker compose up --build --watch

docker-up:
	docker compose up --build --detach

docker-down:
	docker compose down --remove-orphans --rmi all --volumes