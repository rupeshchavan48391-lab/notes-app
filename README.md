# 🚀 Notes App — Complete DevOps & Cloud Deployment Project

<div align="center">

# 📝 Notes App

### Django • Docker • Docker Compose • Nginx • Gunicorn • Docker Hub • AWS EC2 • Kubernetes • Jenkins • GitHub

A production-oriented DevOps project demonstrating how a Django web application can be containerized, deployed to AWS EC2, prepared for Kubernetes orchestration, and integrated into a future Jenkins CI/CD pipeline.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-Orchestration-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker_Hub-Registry-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-181717?style=for-the-badge&logo=github&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Server-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Goals](#-project-goals)
- [Application Features](#-application-features)
- [DevOps Toolchain](#-devops-toolchain)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Complete DevOps Workflow](#-complete-devops-workflow)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Running the Application Locally](#-running-the-application-locally)
- [Running with Docker](#-running-with-docker)
- [Running with Docker Compose](#-running-with-docker-compose)
- [Nginx Configuration](#-nginx-configuration)
- [Gunicorn Configuration](#-gunicorn-configuration)
- [Docker Hub](#-docker-hub)
- [AWS EC2 Deployment](#-aws-ec2-deployment)
- [Kubernetes](#-kubernetes)
- [Kubernetes Namespace](#-kubernetes-namespace)
- [Kubernetes Deployment](#-kubernetes-deployment)
- [Kubernetes Service](#-kubernetes-service)
- [Kubernetes Ingress](#-kubernetes-ingress)
- [Jenkins CI/CD](#-jenkins-cicd)
- [Jenkins Pipeline](#-jenkins-pipeline)
- [Environment Variables](#-environment-variables)
- [Useful Commands](#-useful-commands)
- [Docker vs Kubernetes](#-docker-vs-kubernetes)
- [Security Considerations](#-security-considerations)
- [Troubleshooting](#-troubleshooting)
- [Project Status](#-project-status)
- [Future Improvements](#-future-improvements)
- [DevOps Roadmap](#-devops-roadmap)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

# 📖 Project Overview

**Notes App** is a Django-based web application that has been converted into a complete DevOps-oriented deployment project.

The primary purpose of this project is not only to build a web application, but also to demonstrate the complete lifecycle of deploying and managing an application using modern DevOps technologies.

The application is:

- Developed using Django
- Served using Gunicorn
- Reverse proxied using Nginx
- Containerized using Docker
- Managed locally using Docker Compose
- Published to Docker Hub
- Deployed on AWS EC2
- Prepared for Kubernetes orchestration
- Designed for future Jenkins CI/CD automation
- Managed using Git and GitHub

---

# 🎯 Project Goals

The main objectives of this project are:

1. Build a functional Django web application.
2. Containerize the application using Docker.
3. Run multiple application components using Docker Compose.
4. Use Gunicorn as a production WSGI server.
5. Use Nginx as a reverse proxy.
6. Publish Docker images to Docker Hub.
7. Deploy the application to AWS EC2.
8. Create Kubernetes manifests for future orchestration.
9. Understand Kubernetes Namespaces, Deployments, Services and Ingress.
10. Design a Jenkins CI/CD pipeline.
11. Understand the difference between Docker and Kubernetes.
12. Build a foundation for automated cloud deployment.

---

# ✨ Application Features

The Notes application provides a simple web-based notes system.

Typical application functionality includes:

- 📝 Create notes
- 📖 View notes
- ✏️ Update notes
- 🗑️ Delete notes
- 🌐 Web-based interface
- 🐍 Django backend
- ⚙️ Gunicorn application server
- 🌐 Nginx reverse proxy

The application itself is intentionally simple so that the main focus can remain on **DevOps, deployment, infrastructure and automation**.

---

# 🛠️ DevOps Toolchain

This project uses a complete DevOps-oriented toolchain.

| Tool | Purpose |
|---|---|
| 🐍 Python | Application programming language |
| 🌿 Django | Web application framework |
| ⚙️ Gunicorn | Production WSGI server |
| 🌐 Nginx | Reverse proxy |
| 🐳 Docker | Application containerization |
| 🔗 Docker Compose | Multi-container management |
| 📦 Docker Hub | Container image registry |
| ☁️ AWS EC2 | Cloud compute server |
| 🐧 Ubuntu/Linux | Server operating system |
| ☸️ Kubernetes | Container orchestration |
| 🤖 Jenkins | CI/CD automation |
| 🔧 Git | Version control |
| 🐙 GitHub | Source code hosting |
| 🔐 Environment Variables | Configuration and secrets management |

---

# 💻 Technology Stack

## Application

- Python 3
- Django
- Gunicorn

## Containerization

- Docker
- Dockerfile
- Docker Compose

## Web Server

- Nginx
- HTTP
- Reverse Proxy

## Cloud

- AWS
- EC2
- Ubuntu/Linux

## Container Registry

- Docker Hub

## Orchestration

- Kubernetes
- Namespace
- Deployment
- Pod
- Service
- Ingress

## CI/CD

- Jenkins
- GitHub
- Docker Hub

## Version Control

- Git
- GitHub

---

# 🏗️ Architecture

## Current Docker + AWS Architecture

```text
                         INTERNET
                            │
                            │ HTTP :80
                            ▼
                    ┌─────────────────┐
                    │      NGINX      │
                    │ Reverse Proxy   │
                    │    Container    │
                    │      :80        │
                    └────────┬────────┘
                             │
                             │ Proxy
                             ▼
                    ┌─────────────────┐
                    │    GUNICORN     │
                    │      :8000      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     DJANGO      │
                    │   NOTES APP     │
                    └─────────────────┘
