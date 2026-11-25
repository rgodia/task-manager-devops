
# Task Manager – DevOps Portfolio Project

A simple task management application built with Python Flask and SQLite, designed to demonstrate a complete DevOps lifecycle.

## Technology Stack

- Python 3.12
- Flask
- SQLite
- pytest
- Docker
- Docker Compose
- Git and GitHub

## Features

- Create tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- Persistent SQLite database storage
- Application health endpoint

## Run Locally

Clone the repository:

```bash
git clone git@github.com:rgodia/task-manager-devops.git
cd task-manager-devops
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the application:

```bash
flask --app app.routes run --host=0.0.0.0 --port=5000
```

## Run with Docker Compose

Start the application:

```bash
docker compose up -d --build
```

Access the application at:

http://localhost:5000

Check application health:

```bash
curl http://localhost:5000/health
```

Stop the application:

```bash
docker compose down
```

## Run Automated Tests

```bash
python -m pytest -v
```

## Project Roadmap

- [x] Flask application
- [x] SQLite database
- [x] Automated tests
- [x] GitHub repository
- [x] Docker containerization
- [x] Docker persistent storage
- [x] Docker Compose
- [ ] Jenkins CI/CD
- [ ] GitHub Container Registry
- [ ] Kubernetes deployment with Minikube
- [ ] Development and production environments
- [ ] Prometheus and Grafana monitoring
- [ ] Logging and alerting

## Author

DevOps learning and portfolio project.

