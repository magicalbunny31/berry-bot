DOCKER_DOTENVX = docker run \
	--rm \
	-v "$(PWD)":/app \
	-w /app \
	--user "$$(id -u):$$(id -g)" \
	dotenv/dotenvx

dotenvx-precommit:
	$(DOCKER_DOTENVX) ext precommit

dotenvx-encrypt:
	$(DOCKER_DOTENVX) encrypt -f ./src/.env -fk ./src/.env.keys

dotenvx-decrypt:
	$(DOCKER_DOTENVX) decrypt -f ./src/.env -fk ./src/.env.keys