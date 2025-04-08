# 🐳 Dockerfile — Full Tutorial with Flask Example

> Learn how to write a complete Dockerfile from scratch with explanations and real Flask application.

---

## 🤔 What is a Dockerfile?

A **Dockerfile** is a text document containing instructions to build a Docker image automatically.

Think of it like a recipe: Docker reads the instructions and creates an image step by step.

---

## 🧱 Basic Dockerfile Instructions

| Instruction | Description                                  |
|-------------|----------------------------------------------|
| `FROM`      | Sets the base image                         |
| `WORKDIR`   | Sets working directory inside the container |
| `COPY`      | Copies files from host to container         |
| `RUN`       | Executes commands during image build        |
| `CMD`       | Default command to run when container starts|
| `EXPOSE`    | Declares container port to expose           |

---

## 📦 Create a Flask App with Dockerfile

### 📁 Directory Structure
```
docker-flask-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

### 🔸 app.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 🔸 requirements.txt
```
flask
```

### 🔸 Dockerfile
```dockerfile
# Step 1: Use a base image
FROM python:3.9-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files into container
COPY . /app

# Step 4: Install dependencies
RUN pip install -r requirements.txt

# Step 5: Expose port
EXPOSE 5000

# Step 6: Set default command
CMD ["python", "app.py"]
```

---

## 🚀 Build & Run

```bash
# Build image from Dockerfile
docker build -t flask-dockerfile-app .

# Run the container
docker run -d -p 5000:5000 flask-dockerfile-app
```

🔗 Visit: http://localhost:5000 → Output: Hello from Dockerized Flask App!

---

## 🧪 Additional Dockerfile Instructions

### 🧹 `.dockerignore`
Avoid copying unwanted files into the image.

```
__pycache__/
*.pyc
*.pyo
*.log
.git
```

### 🧪 Multi-Stage Build (for optimization)
```dockerfile
FROM python:3.9-slim AS base
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

FROM base AS production
CMD ["python", "app.py"]
```

---

## 🛠️ Best Practices

- Use `.dockerignore` to keep images small
- Pin versions in `requirements.txt`
- Use multi-stage builds for complex apps
- Keep layers minimal and cacheable
- Always specify a base image (avoid `latest`)

---

## 🧽 Cleanup Commands

```bash
docker ps -a            # List containers
docker stop <id>        # Stop container
docker rm <id>          # Remove container
docker rmi flask-dockerfile-app  # Remove image
```

---

## ✅ Summary

- Dockerfile automates image creation
- Every instruction creates a new layer
- Best used for deploying applications reproducibly

---

## 📚 Learn More

- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

Happy Docking! 🐋



