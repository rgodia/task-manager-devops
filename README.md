# Task Manager – DevOps Portfolio Project

A Flask-based task management application developed as a hands-on DevOps
portfolio project. The project demonstrates application development,
automated testing, containerization, CI infrastructure, and a planned
Kubernetes deployment.

The environment is an Ubuntu virtual machine running Docker and Jenkins.

## Project Status

**Current focus:** Jenkins CI infrastructure and pipeline validation.

Completed:
- Flask task management application with SQLite.
- Automated application tests using pytest.
- Docker image and Docker Compose configuration.
- Jenkins controller running in Docker.
- Separate Jenkins Python inbound build agent.
- Jenkins CI pipeline configured for GitHub checkout and pytest.
- Jenkins infrastructure defined using Docker Compose.
- Persistent Jenkins data and agent workspace volumes.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python / Flask | Application and web framework |
| SQLite | Application database |
| pytest | Automated testing |
| Git / GitHub | Version control and source hosting |
| Ubuntu | Development environment |
| Docker | Application and CI containerization |
| Docker Compose | Container management |
| Jenkins | CI automation |
| Java 21 | Jenkins runtime |
| Minikube / Kubernetes | Planned orchestration |
| Prometheus / Grafana | Planned monitoring |

## Application Features

- Create and view tasks.
- Mark tasks as completed.
- Delete tasks.
- SQLite database integration.
- Configurable database location.
- Application health endpoint.
- Persistent database storage using Docker volumes.

## Project Architecture

The current environment contains the following components:

```text
Ubuntu VM
|
+-- Git / GitHub
|   |
|   +-- Task Manager source code
|   +-- Jenkinsfile
|   +-- Docker configuration
|
+-- Docker
    |
    +-- Task Manager application
    |   +-- Flask
    |   +-- SQLite
    |   +-- Persistent database volume
    |
    +-- Jenkins infrastructure
        |
        +-- Jenkins controller
        |   +-- Jenkins UI
        |   +-- Pipeline configuration
        |   +-- Persistent Jenkins home
        |
        +-- Python inbound agent
            +-- Python
            +-- Git
            +-- Java 21
            +-- Docker CLI
            +-- pytest (installed through project dependencies)
