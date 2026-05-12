# Get base image
FROM python:3.9-slim  

# Set working directory
WORKDIR /app

# Install curl and delete apt cache to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

#Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user and switch to it for better security
RUN adduser --disabled-password --gecos '' appuser
COPY . .
USER appuser

# Container listens on port 5000
EXPOSE 5000

#Run health check to ensure API is responsive every 30 seconds
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]
