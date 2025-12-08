# AI Council - Prompt Injection Generator

API do generowania prompt injection z wykorzystaniem trzech modeli załadowanych lokalnie.

## Modele

- **llama** (Llama-3.1-8B-Instruct) - Kreatywne generowanie payloadów, 8B parametrów
- **mistral** (Mistral-7B-Instruct-v0.3) - Rozumienie i obchodzenie zabezpieczeń, 7B parametrów
- **gemma** (Gemma-2-9B-IT) - Analiza i tworzenie wariantów, 9B parametrów

## Wymagania

- Python 3.14+
- CUDA (dla GPU) lub CPU (wolniejsze)
- ~30GB RAM dla wszystkich modeli
- Tokeny HuggingFace dla modeli Llama/Gemma

## Instalacja

```bash
# Zainstaluj zależności
poetry install

# Zaloguj się do HuggingFace (wymagane dla Llama i Gemma)
huggingface-cli login
```

## Uruchomienie

```bash
python main.py
```

API będzie dostępne na `http://localhost:8000`

Modele są ładowane przy pierwszym użyciu (lazy loading).

## Przykłady użycia

```bash
# Llama
curl -X POST http://localhost:8000/llama \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Generate a prompt injection to bypass content filters"}'

# Mistral
curl -X POST http://localhost:8000/mistral \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Create SQL injection payload"}'

# Gemma
curl -X POST http://localhost:8000/gemma \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Generate XSS attack variants"}'
```

## Dokumentacja API

Interaktywna dokumentacja: `http://localhost:8000/docs`
