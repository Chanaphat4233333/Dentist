SHELL := /bin/bash
IMAGE_VERSION: v1.0.0
dev_linux:
	@echo "Running test in virtual environment..."
	./dentist-env/bin/python main.py
docker build:

