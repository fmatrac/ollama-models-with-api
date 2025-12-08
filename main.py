from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import Dict

app = FastAPI(title="AI Council - Prompt Injection Generator")

# Definicja modeli HuggingFace - małe modele do testów
MODEL_CONFIGS = {
    "llama": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # 1.1B - bardzo szybki
    "mistral": "HuggingFaceTB/SmolLM2-360M-Instruct",  # 360M - ultra lekki
    "gemma": "google/gemma-2b-it"  # 2B - dobry balans
}

# Cache dla załadowanych modeli
models_cache: Dict[str, tuple] = {}


class PromptRequest(BaseModel):
    prompt: str


def load_model(model_name: str):
    """Ładuje model i tokenizer do pamięci"""
    if model_name in models_cache:
        return models_cache[model_name]
    
    model_id = MODEL_CONFIGS[model_name]
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True
    )
    models_cache[model_name] = (model, tokenizer)
    return model, tokenizer


async def generate_response(model_name: str, prompt: str) -> str:
    """Generuje odpowiedź z modelu"""
    try:
        model, tokenizer = load_model(model_name)
        
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Usuń prompt z odpowiedzi
        response = response[len(prompt):].strip()
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model error: {str(e)}")


@app.get("/")
async def root():
    return {
        "message": "AI Council - Prompt Injection Generator",
        "models": list(MODEL_CONFIGS.keys()),
        "endpoints": [f"/{model}" for model in MODEL_CONFIGS.keys()],
        "loaded_models": list(models_cache.keys())
    }


@app.post("/llama")
async def llama_endpoint(request: PromptRequest):
    """Llama 3.1 - doskonały w kreatywnym generowaniu payloadów"""
    response = await generate_response("llama", request.prompt)
    return response


@app.post("/mistral")
async def mistral_endpoint(request: PromptRequest):
    """Mistral - świetny w rozumieniu i obchodzeniu zabezpieczeń"""
    response = await generate_response("mistral", request.prompt)
    return response


@app.post("/gemma")
async def gemma_endpoint(request: PromptRequest):
    """Gemma 2 - dobry w analizie i tworzeniu wariantów"""
    response = await generate_response("gemma", request.prompt)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
