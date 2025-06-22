# AI/ML Football Analysis System with YOLO

## Prerequisites
- Docker and Docker Compose installed on your system
- Python (^3.13.0) installed on your system
- Node.js (^20.0) and npm installed on your system

## Quick Start
- Clone the repository:

  ```bash
  git clone https://github.com/RockyNiu/nextjs-fastapi.git
  cd nextjs-fastapi
  ```
- Follow the instructions in [backend/README.md](backend/README.md) to add secret files in the folder `backend/config`
- Start the application:
  ```bash
  cd docker
  docker compose -f docker-compose.yml -f docker-compose-frontend.yml up -d --build
  ```

- Open http://localhost:3000 in your browser to see the frontend.
- The API will be available at http://localhost:8000.

## Development Setup
### Backend Development
- Navigate to the backend directory:
  ```bash
  cd backend
  ```
- Start the backend in debug mode:
  ```bash
  cd ../docker
  docker compose -f docker-compose.yml -f docker-compose-debug.yml up -d
  ```
- Use Visual Studio Code to debug the backend.
  ```text
  {
      "name": "Backend: debug in docker",
      "type": "python",
      "request": "attach",
      "port": 5678,
      "host": "127.0.0.1",
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}/backend",
          "remoteRoot": "/app"
        }
      ]
    },
  ```

### Frontend Development
- Navigate to the frontend directory:
  ```bash
  cd frontend
  ```

- Follow the instructions in [frontend/README.md](frontend/README.md) for local setup.
- Start the frontend development server as per the README instructions.
- Modify frontend code in your preferred editor (VS Code recommended).

## Project Structure
```text
nextjs-fastapi/
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routers/
│   │   │   └── middleware.py
│   │   ├── config/
│   │   │   ├── .secrets.development.toml
│   │   │   ├── .secrets.test.toml
│   │   │   ├── settings.development.toml
│   │   │   └── settings.test.toml
│   │   ├── db/
│   │   │   ├── dao/
│   │   │   ├── orm/
│   │   │   ├── service/
│   │   │   ├── base_dao.py
│   │   │   └── database.py
│   │   ├── entities/
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   │   ├── db/
│   │   ├── utils
│   │   │   ├── fixtures/
│   │   └── conftest.py
│   ├── .gitignore
│   ├── .pre-commit-config.yaml
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── Makefile
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   └── ruff.toml
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   └── services/
│   ├── .eslintrc.json
│   ├── .gitignore
│   ├── .prettierignore
│   ├── .prettierrc
│   ├── Dockerfile
│   ├── next.config.mjs
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── .gitignore
├── docker/
│   ├── docker-compose.yml
│   ├── docker-compose-frontend.yml
│   └── docker-compose-debug.yml
├── .gitignore
└── README.md
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
## License
Free. No restrictions.
