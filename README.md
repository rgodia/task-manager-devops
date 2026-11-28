
# Task Manager – DevOps Portfolio Project

A Flask-based task management application built to demonstrate an end-to-end DevOps lifecycle, from application development to automated CI/CD, containerization, Kubernetes deployment, and monitoring.

This project is being developed incrementally on an Ubuntu virtual machine.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development and CI build environment |
| Flask | Web application framework |
| SQLite | Database |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |
| Docker | Application and CI containerization |
| Docker Compose | Container management |
| Jenkins | Continuous Integration / Continuous Deployment |
| Java 21 | Jenkins runtime |
| Minikube | Planned local Kubernetes environment |
| Prometheus | Planned monitoring and metrics |
| Grafana | Planned monitoring dashboards |

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
    |      +-- Docker configuration
    |
    +-- Docker
           |
           +-- Task Manager container
           |      |
           |      +-- Flask application
           |      +-- SQLite database
           |      +-- Persistent Docker volume
           |
           +-- Jenkins infrastructure (Docker Compose)
                  |
                  +-- Jenkins controller
                  |      |
                  |      +-- Jenkins LTS / Java 21
                  |      +-- Jenkins jobs
                  |      +-- Pipeline configuration
                  |      +-- Persistent Jenkins home
                  |
                  +-- Python inbound agent
                         |
                         +-- Python
                         +-- Git
                         +-- Java 21
                         +-- Docker CLI
                         +-- Docker Buildx
                         +-- Persistent agent workspace

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

## Jenkins CI Infrastructure

Jenkins is used to automate the application's continuous integration process.

The infrastructure is defined using Docker Compose and consists of a Jenkins controller and a separate Python inbound build agent.

### Jenkins Architecture

- Jenkins controller runs inside Docker using the official Jenkins LTS image with Java 21.
- A custom Python inbound agent runs separately from the controller.
- The agent connects to the controller using the Jenkins WebSocket protocol.
- GitHub provides the source code.
- Jenkins uses a Jenkinsfile stored in the repository.
- Docker Compose manages both Jenkins services.
- Named Docker volumes preserve Jenkins controller data and agent workspace data.

### Jenkins Controller

The controller is built using:

    jenkins/controller/Dockerfile

It uses the Jenkins LTS Java 21 image and exposes the web interface on port 8080.

### Python Inbound Agent

The agent image is built using:

    jenkins/python-agent/Dockerfile

The custom agent image includes:

- Python
- Git
- Java 21
- Docker CLI
- Docker Buildx

The agent is configured with the Jenkins label:

    python

The Jenkins pipeline uses this label to execute CI jobs on the Python agent rather than the controller.

The agent has access to the host Docker socket to build and inspect Docker images.

**Security consideration:** Docker socket access is highly privileged and can provide effective control over the Docker host. Only trusted pipeline code should execute on this agent.

### Jenkins Docker Compose Configuration

The infrastructure is defined in:

    jenkins/docker-compose.yaml

It defines two services:

- `jenkins` — Jenkins controller.
- `python-agent` — Python inbound build agent.

Persistent Docker volumes are used for:

- Jenkins controller data and configuration.
- Agent Jenkins data.
- Agent workspace.

The Compose configuration uses an external Docker network and existing external volumes to preserve infrastructure data across container recreation.

### Jenkins Environment Configuration

An example environment file is provided:

    jenkins/.env.example

Create a local environment file:

    cd jenkins
    cp .env.example .env

Configure the Jenkins inbound agent secret in `.env`.

Start the Jenkins infrastructure:

    docker compose up -d --build

Check service status:

    docker compose ps

View logs:

    docker compose logs -f

The actual `.env` file contains a Jenkins agent secret and must never be committed to GitHub. It is excluded through `.gitignore`.

## Jenkins CI Pipeline

Jenkins automates application testing and Docker image creation using the Jenkinsfile in the repository root.

### Current CI Pipeline Stages

The pipeline executes on the Python agent using the `python` label.

1. **Checkout** — retrieves source code from GitHub.
2. **Install Dependencies** — creates a Python virtual environment and installs dependencies from `requirements.txt`.
3. **Run Tests** — executes automated tests using pytest.
4. **Build Docker Image** — builds the Task Manager Docker image.
5. **Verify Docker Image** — inspects both generated image tags to confirm that the images exist.

### Docker Image Tagging

The pipeline creates two image tags:

    task-manager:latest

    task-manager:<12-character Git commit hash>

The commit-specific tag makes it possible to identify which source revision produced a particular Docker image.

### Pipeline Configuration

The pipeline definition is stored in:

    Jenkinsfile

The pipeline uses:

    agent {
        label 'python'
    }

Docker image building is performed by the Python agent through its Docker CLI access to the host Docker socket.

The pipeline includes post-build success, failure, and completion messages.

**Current focus:** Validate the complete Jenkins pipeline, including the Docker image build and verification stages.

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
- [x] Custom Jenkins controller Docker image
- [x] Custom Python inbound agent Docker image
- [x] Jenkins infrastructure Docker Compose configuration
- [x] Persistent Jenkins controller and agent volumes
- [x] Jenkins agent WebSocket connectivity
- [x] Jenkins Docker image build stage implemented
- [x] Docker image verification stage implemented

### Upcoming

- [ ] Validate the complete Jenkins pipeline end to end
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
- Docker Compose
- Jenkins controller and agent architecture
- Container registries
- Kubernetes orchestration
- Infrastructure monitoring
- Logging and alerting
- Application reliability and scalability

## Author

DevOps learning and portfolio project.

GitHub:

https://github.com/rgodia/task-manager-devops

