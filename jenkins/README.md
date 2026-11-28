# Jenkins CI Infrastructure

This directory contains the Docker-based Jenkins infrastructure for the
Task Manager DevOps project.

## Architecture

- **Jenkins controller:** Runs the Jenkins LTS controller using Java 21.
- **Python agent:** Connects to the controller over the Jenkins WebSocket
  protocol and provides Python, Git, Java, and Docker CLI tools.
- **Docker Compose:** Defines the controller and agent services.
- **Persistent volumes:** Preserve Jenkins controller data and agent workspace
  data across container restarts.

The Python agent has access to the host Docker socket so that trusted CI jobs
can build Docker images. Treat this access as privileged.

## Prerequisites

- Docker Engine
- Docker Compose plugin
- A running Jenkins controller configuration
- The external Docker network and volumes referenced in `docker-compose.yaml`

## Configuration

Create a local environment file from the example:

```bash
cp .env.example .env
