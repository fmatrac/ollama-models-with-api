FROM python:3.12-slim

WORKDIR /app

# Zainstaluj poetry
RUN pip install poetry

# Skopiuj pliki projektu
COPY pyproject.toml ./
COPY main.py ./

# Zainstaluj zależności
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Expose port
EXPOSE 8080

# Uruchom aplikację
CMD ["python", "main.py"]
