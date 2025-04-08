# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create a volume for persistent database storage
VOLUME /app/instance

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]