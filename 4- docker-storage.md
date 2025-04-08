# 📆 Docker Storage — Full Tutorial with Flask Example

> Learn how to persist data in Docker using **Volumes**, **Bind Mounts**, and **tmpfs** — with a real Flask app demo.

---

## 🧠 Why Storage in Docker?

By default, Docker containers are **ephemeral**—once stopped or removed, any data inside is lost. Docker provides **storage solutions** to persist or manage data across containers or sessions.

---

## 🏗️ Types of Docker Storage

| Type        | Managed By | Persistent | Use Case                           |
|-------------|------------|------------|------------------------------------|
| **Volume**  | Docker     | ✅ Yes     | Best for persistent app data       |
| **Bind Mount** | Host OS | ✅ Yes     | Dev workflows, code syncing        |
| **tmpfs**   | RAM        | ❌ No      | Temporary, in-memory secure data   |

---

## 1⃣ Docker Volumes (Best Practice ✅)

### 🔹 What is a Volume?
A **Docker Volume** is a managed directory outside the container filesystem, designed for persistent data storage.

### 🔹 Volume Commands

```bash
# Create a volume
docker volume create myvol

# List all volumes
docker volume ls

# Inspect a volume
docker volume inspect myvol

# Remove a volume
docker volume rm myvol
```

---

### 🧪 Volume Example with Flask App

**📁 Directory Structure**
```
docker-flask-volume/
├── app.py
├── requirements.txt
├── Dockerfile
└── message.txt
```

**🔸 app.py**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    with open("/data/message.txt", "r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**🔸 requirements.txt**
```
flask
```

**🔸 Dockerfile**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

**🔸 message.txt**
```
Hello from Docker Volume!
```

---

### 🚀 Run Flask App with Volume

```bash
# Build image
docker build -t flask-vol-app .

# Create named volume
docker volume create flask_data

# Copy message.txt into the volume using temporary container
docker container create --name temp -v flask_data:/data alpine
docker cp message.txt temp:/data/message.txt
docker rm temp

# Run container with volume mounted
docker run -d -p 5000:5000 -v flask_data:/data flask-vol-app
```

🧪 Visit: http://localhost:5000 → Output: Hello from Docker Volume!

---

## 2⃣ Bind Mounts (Host ↔ Container)

### 🔹 What is a Bind Mount?

A **Bind Mount** maps a **specific host path** to a container path. It allows live editing and host-container sync, great for development.

### 🧪 Flask App with Bind Mount

```bash
# Create local folder and message file
mkdir ~/docker-data
echo "Bind mount says hello!" > ~/docker-data/message.txt

# Run container and mount host dir
docker run -d -p 5001:5000 -v ~/docker-data:/data flask-vol-app
```

🧪 Visit: http://localhost:5001 → Output: Bind mount says hello!

---

### 🔸 Use Cases for Bind Mounts
- Live code changes (local dev)
- Access host logs/configs
- Mount .env files, configs, secrets in dev

⚠️ Not recommended for production due to permission/security concerns.

---

## 3⃣ tmpfs Mounts (RAM Storage)

### 🔹 What is tmpfs?

tmpfs mounts create **RAM-based filesystems** in containers. They're **fast**, temporary, and **auto-wipe on container stop**.

### 🧪 tmpfs Example

```bash
docker run -d -p 5002:5000 \
  --tmpfs /data:rw,size=64m \
  flask-vol-app
```

🧪 Visit: http://localhost:5002 → May error unless `/data/message.txt` is created manually inside the container.

### 🧪 Enter container and test

```bash
docker exec -it <container_id> bash
echo "This lives in RAM!" > /data/message.txt
exit
```

🧪 Refresh browser → Output: This lives in RAM!

---

## 🔍 Volume vs Bind Mount vs tmpfs

| Feature               | Volume        | Bind Mount     | tmpfs        |
|-----------------------|---------------|----------------|--------------|
| Persistent            | ✅ Yes         | ✅ Yes         | ❌ No        |
| Managed by Docker     | ✅ Yes         | ❌ No          | ✅ Yes       |
| Recommended for Prod  | ✅ Yes         | ❌ No          | ⚠️ Conditional|
| Use in Dev            | ⚠️ Possible     | ✅ Ideal        | ⚠️ Rare       |
| Speed (read/write)    | Medium         | High           | 🔥 Fastest   |

---

## 🧼 Cleanup Commands

```bash
docker container stop $(docker ps -q)
docker container rm $(docker ps -aq)
docker volume rm flask_data
docker system prune -a --volumes
```

---

## 📌 Summary

- **Volumes**: Best for persistent, production-ready storage.
- **Bind Mounts**: Best for live development and debugging.
- **tmpfs**: Fastest, secure for temporary data (in memory).

---

## 📚 Further Learning

- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Docker Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
- [Docker tmpfs](https://docs.docker.com/storage/tmpfs/)

---

Happy Docking! 🐳