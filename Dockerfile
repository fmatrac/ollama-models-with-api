FROM python:3.12-slim

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

<<<<<<< HEAD
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
=======
# Zainstaluj zależności
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root
>>>>>>> 0680e6d923cab9269d0ae2175ac599c80de8b7c5

EXPOSE 8080

CMD ["python", "main.py"]

