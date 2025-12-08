# AI Council - Prompt Injection Generator

API do generowania prompt injection z wykorzystaniem trzech modeli Ollama.

## Modele

- **llama** (llama3.1:8b) - Kreatywne generowanie payloadów, 8B parametrów
- **mistral** (mistral:7b) - Rozumienie i obchodzenie zabezpieczeń, 7B parametrów
- **gemma** (gemma2:9b) - Analiza i tworzenie wariantów, 9B parametrów

## Instalacja

```bash
# Zainstaluj zależności
poetry install

# Pobierz modele Ollama
ollama pull llama3.1:8b
ollama pull mistral:7b
ollama pull gemma2:9b
```

## Uruchomienie

```bash
python main.py
```

API będzie dostępne na `http://localhost:8000`

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
