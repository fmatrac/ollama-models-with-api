from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="AI Council - Prompt Injection Generator")

# Konfiguracja Ollama
OLLAMA_BASE_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

# Definicja modeli - dobre w generowaniu prompt injection
MODELS = {
    "llama": "llama3.1:8b",      # 8B parametrów - balans między szybkością a jakością
    "mistral": "mistral:7b",     # 7B parametrów - doskonały do adversarial prompts
    "gemma": "gemma2:9b"         # 9B parametrów - najlepszy w analizie zabezpieczeń
}


class PromptRequest(BaseModel):
    prompt: str


async def query_ollama(model: str, prompt: str) -> str:
    """Wysyła zapytanie do Ollama i zwraca odpowiedź"""
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")


@app.get("/")
async def root():
    return {
        "message": "AI Council - Prompt Injection Generator",
        "models": list(MODELS.keys()),
        "endpoints": [f"/{model}" for model in MODELS.keys()]
    }


@app.post("/llama")
async def llama_endpoint(request: PromptRequest):
    """Llama 3.1 - doskonały w kreatywnym generowaniu payloadów"""
    response = await query_ollama(MODELS["llama"], request.prompt)
    return response


@app.post("/mistral")
async def mistral_endpoint(request: PromptRequest):
    """Mistral - świetny w rozumieniu i obchodzeniu zabezpieczeń"""
    response = await query_ollama(MODELS["mistral"], request.prompt)
    return response


@app.post("/gemma")
async def gemma_endpoint(request: PromptRequest):
    """Gemma 2 - dobry w analizie i tworzeniu wariantów"""
    response = await query_ollama(MODELS["gemma"], request.prompt)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
