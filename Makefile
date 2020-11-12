SHELL := /bin/bash
DOCKER_IMAGE=cynnexis/tyme

.PHONY: all help test clean

all:
	$(MAKE) help; \
	exit 1

help:
	@echo "Tyme Makefile"
	@echo ''
	@echo "This Makefile helps you build and run Tyme."
	@echo ''
	@echo "  configure           - Configure the project."
	@echo "  test                - Run the tests."
	@echo "  lint                - Run YAPF to check if the Python scripts are syntaxically correct."
	@echo "  fix-lint            - Run YAPF to fix the lint in the Python files."
	@echo "  clean               - Clean the projects."
	@echo "  docker-build        - Build the Docker image given by the Dockerfile."
	@echo "  docker-down         - Down docker-compose."
	@echo "  docker-test-up      - Use docker-compose to launch the tests."
	@echo "  docker-test-restart - Use docker-compose to restart the tests."
	@echo "  docker-kill         - Stop and remove all containers, dangling images and unused networks and volumes. Be careful when executing this command!"

.git/hooks/pre-commit:
	curl -fsSL "https://gist.githubusercontent.com/Cynnexis/cd7fdc7b911ac39b623a3a62105e7d45/raw/pre-commit" -o ".git/hooks/pre-commit"
	dos2unix ".git/hooks/pre-commit"

.git/hooks/post-commit:
	curl -fsSL "https://gist.githubusercontent.com/Cynnexis/b79ea3a883073711b342273b646acf3c/raw/post-commit" -o ".git/hooks/post-commit"
	dos2unix ".git/hooks/post-commit"

configure-git: .git/hooks/pre-commit .git/hooks/post-commit

configure: configure-git
	pip install -r requirements.txt

test:
	@./docker-entrypoint.sh test

lint:
	@./docker-entrypoint.sh lint

fix-lint:
	@./docker-entrypoint.sh fix-lint

build-docker:
	docker build -t $(DOCKER_IMAGE) .

docker-down:
	docker-compose down --remove-orphans --volumes

docker-test:
	docker run --rm $(DOCKER_IMAGE) test

docker-test-up:
	docker-compose up -d --remove-orphans test lint

docker-test-restart: docker-down
	$(MAKE) docker-test-up

docker-kill:
	docker rm -f $$(docker ps -aq) || docker rmi -f $$(docker images -f "dangling=true" -q) || docker system prune -f
