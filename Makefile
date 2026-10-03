.PHONY: build build-linux up up-linux down down-linux dev dev-linux dev-backend dev-backend-linux dev-frontend dev-frontend-linux install install-linux logs logs-linux restart restart-linux

# --- Windows ---
build:
	docker-compose build

up:
	@powershell -Command "if (-not (Test-Path 'backend\.env')) { Copy-Item 'backend\.env.example' 'backend\.env' }"
	docker-compose up -d
	@echo   Frontend : http://localhost:5173
	@echo   API docs : http://localhost:8000/docs

down:
	docker-compose down

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

dev-backend:
	@powershell -Command "if (-not (Test-Path 'backend\.env')) { Copy-Item 'backend\.env.example' 'backend\.env' }"
	cd backend && uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

dev:
	$(MAKE) -j2 dev-backend dev-frontend

logs:
	docker-compose logs -f

restart:
	docker-compose restart


# --- Linux ---
build-linux:
	docker-compose build

up-linux:
	@if [ ! -f backend/.env ]; then cp backend/.env.example backend/.env; fi
	docker-compose up -d
	@echo   Frontend : http://localhost:5173
	@echo   API docs : http://localhost:8000/docs

down-linux:
	docker-compose down

install-linux:
	cd backend && python -m venv venv && ./venv/bin/pip install -r requirements.txt
	cd frontend && npm install

dev-backend-linux:
	@if [ ! -f backend/.env ]; then cp backend/.env.example backend/.env; fi
	cd backend && ./venv/bin/uvicorn app.main:app --reload --port 8000

dev-frontend-linux:
	cd frontend && npm run dev

dev-linux:
	$(MAKE) -j2 dev-backend-linux dev-frontend-linux

logs-linux:
	docker-compose logs -f

restart-linux:
	docker-compose restart
