#Use small Python 3.9 image as base
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and set entry point
COPY . .
ENTRYPOINT ["python"]
CMD ["report.py"]
