FROM python:3.14-slim

# Install build tools needed to compile numpy & friends
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install poetry (if you really need it)
RUN pip install --no-cache-dir poetry

# Copy project files
COPY main.py ./
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]

