# Docker vs Native Flask Example

This project demonstrates why Docker is essential by showing:
- ❌ How the app **fails** when run natively (due to Linux dependencies)
- ✅ How it **works perfectly** in Docker

[![Docker Build](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://docs.docker.com/get-docker/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-green?logo=python)](https://www.python.org/downloads/)

## 📥 Clone the Repository
```bash
git clone https://github.com/ft4bhi/docker_example.git
cd docker_example
```

## 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
## 2. Install Requirements
```bash
pip install -r requirements.txt
```
## 3. Run the App 
```bash
python app.py
```
## Expected Error:
ModuleNotFoundError: No module named 'grp'

### ✅ Docker Execution (Only Working Method)

## 1. Build Docker Image
```bash
docker build -t flask-docker .
```
## 2. Run the Container
```bash
docker run -p 5000:5000 flask-docker
```
