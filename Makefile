VENV_DIR = .venv
PIP = $(VENV_DIR)/bin/pip


$(VENV_DIR):  ## Create virtual environment
	@python3 -m venv $(VENV_DIR)

run-app: # Build app using docker compose
	@echo "Building app using docker compose"
	@docker compose -f docker-compose.yml -f docker-compose.override.yml up --build


