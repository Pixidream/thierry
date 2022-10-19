dockerFile := docker-compose.dev.yml
requirements := $(dockerFile) .env.dev

dev: $(requirements)
	docker compose -f $(dockerFile) up --build -d

stop: $(requirements)
	docker compose -f $(dockerFile) down --remove-orphans

stop-clean: $(requirements)
	docker compose -f $(dockerFile) down --remove-orphans --volumes

pre-commit: pyproject.toml
	poetry run pre-commit run --all-files

test: $(requirements)
	docker compose -f $(dockerFile) exec web poetry run pytest
