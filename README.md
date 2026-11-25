
# Task Manager – DevOps Portfolio Project

A Flask-based task management application built to demonstrate an end-to-end DevOps lifecycle, from application development to automated CI/CD, containerization, Kubernetes deployment, and monitoring.

This project is being developed incrementally on an Ubuntu virtual machine.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Flask | Web application framework |
| SQLite | Database |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |
| Docker | Application containerization |
| Docker Compose | Container management |
| Jenkins | Continuous Integration / Continuous Deployment |
| Minikube | Local Kubernetes environment |
| Prometheus | Monitoring and metrics |
| Grafana | Monitoring dashboards |

## Application Features

- Create tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- SQLite database integration
- Configurable database location
- Application health endpoint
- Persistent database storage with Docker volumes

## Project Architecture

Current architecture:

    Ubuntu VM
    |
    +-- Git / GitHub
    |      |
    |      +-- Source code
    |      +-- Jenkinsfile
    |
    +-- Docker
           |
           +-- Task Manager container
           |      |
           |      +-- Flask application
           |      +-- SQLite database
           |      +-- Persistent Docker volume
           |
           +-- Jenkins controller
           |      |
           |      +-- Jenkins jobs
           |      +-- Pipeline configuration
           |
           +-- Jenkins Python build agent
                  |
                  +-- Python
                  +-- Git
                  +-- pytest

## Run Locally

Clone the repository:

    git clone git@github.com:rgodia/task-manager-devops.git
    cd task-manager-devops

Create a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run the application:

    flask --app app.routes run --host=0.0.0.0 --port=5000

Access the application:

    http://localhost:5000

## Run Automated Tests

Activate the virtual environment:

    source venv/bin/activate

Run pytest:

    python -m pytest -v

## Run with Docker

Build the Docker image:

    docker build -t task-manager:1.1 .

Run the container:

    docker run -d \
      --name task-manager \
      -p 5000:5000 \
      -e DATABASE_PATH=/data/tasks.db \
      -v task-manager-data:/data \
      task-manager:1.1

Check running containers:

    docker ps

View container logs:

    docker logs task-manager

## Run with Docker Compose

Start the application:

    docker compose up -d --build

Check container status:

    docker compose ps

View logs:

    docker compose logs -f

Check application health:

    curl http://localhost:5000/health

Stop the application:

    docker compose down

Note: Docker named volumes are used to persist SQLite data independently of the application container.

## Jenkins CI Pipeline

Jenkins is used to automate the application's continuous integration process.

### Jenkins Architecture

- Jenkins controller runs inside Docker.
- A separate Python build agent executes pipeline jobs.
- GitHub provides the source code.
- Jenkins uses a Jenkinsfile stored in the repository.

### Current CI Pipeline Stages

1. Checkout source code from GitHub.
2. Create a Python virtual environment.
3. Install application dependencies.
4. Execute automated tests using pytest.
5. Report pipeline success or failure.

### Pipeline Configuration

The pipeline is defined in:

    Jenkinsfile

The Python build agent is configured with the label:

    python

The pipeline currently executes successfully.

## Project Roadmap

### Completed

- [x] Ubuntu development environment
- [x] Flask application development
- [x] SQLite database integration
- [x] CRUD functionality
- [x] Automated tests with pytest
- [x] GitHub repository
- [x] Git version control
- [x] Dockerfile
- [x] Docker image creation
- [x] Docker persistent volumes
- [x] Docker Compose
- [x] Jenkins controller installation
- [x] Jenkins Python build agent
- [x] Jenkinsfile
- [x] GitHub source code checkout through Jenkins
- [x] Automated pytest execution through Jenkins

### Upcoming

- [ ] Automate Docker image builds through Jenkins
- [ ] Publish Docker images to GitHub Container Registry (GHCR)
- [ ] Configure GitHub webhooks for automatic builds
- [ ] Install Minikube
- [ ] Deploy application to Kubernetes
- [ ] Configure Kubernetes Services and Deployments
- [ ] Configure Kubernetes PersistentVolumes and PersistentVolumeClaims
- [ ] Configure application replicas and scaling
- [ ] Implement development and production environments
- [ ] Automate Kubernetes deployments through Jenkins
- [ ] Configure deployment verification and rollback
- [ ] Implement Prometheus monitoring
- [ ] Create Grafana dashboards
- [ ] Configure centralized logging
- [ ] Implement alerting
- [ ] Explore high availability and resilience

## Learning Objectives

This project is intended to demonstrate practical experience with:

- Linux administration
- Python application development
- Git and GitHub
- Automated testing
- CI/CD pipelines
- Docker and containerization
- Jenkins automation
- Container registries
- Kubernetes orchestration
- Infrastructure monitoring
- Logging and alerting
- Application reliability and scalability

## Author

DevOps learning and portfolio project.

GitHub:
https://github.com/rgodia/task-manager-devops

