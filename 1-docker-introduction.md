# Docker Introduction

## What is Docker?
- A platform that uses OS-level virtualization to deliver software in packages called containers.
- Containers are lightweight, fast, and provide consistent environments for running applications.

## Key Concepts
- **Docker Image**: A lightweight, standalone, executable package that includes everything needed to run a piece of software.
- **Docker Container**: A running instance of a Docker image.
- **Dockerfile**: A text file that contains all commands to build a Docker image.
- **Docker Hub**: A cloud-based repository for Docker images.

## Key Docker Commands
- **docker --version**: Check Docker version.
- **docker pull [image-name]**: Pull a Docker image from Docker Hub.
- **docker build -t [image-name] .**: Build a Docker image from the current directory.
- **docker run -d -p 5000:5000 [image-name]**: Run a Docker container in detached mode, exposing port 5000.
- **docker ps**: List running containers.
- **docker stop [container-id]**: Stop a running container.
- **docker rm [container-id]**: Remove a stopped container.
- **docker rmi [image-id]**: Remove a Docker image.
