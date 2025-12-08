# AI Council - Prompt Injection Generator

API do generowania prompt injection z wykorzystaniem trzech modeli załadowanych lokalnie.

## Modele (testowe - małe wersje)

- **llama** (TinyLlama-1.1B) - 1.1B parametrów
- **mistral** (SmolLM2-360M) - 360M parametrów
- **gemma** (Gemma-2B-IT) - 2B parametrów

## Wymagania

- Python 3.14+
- CUDA (dla GPU) lub CPU
- ~4GB RAM dla wszystkich modeli

## Instalacja

```bash
# Zainstaluj zależności
poetry install
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
