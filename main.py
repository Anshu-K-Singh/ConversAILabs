from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])


CONFIG = {
    "vapi": {
        "url": "https://api.vapi.ai/assistant",
        "api_key": "4bc34965-44c5-4196-9442-1a08627b06f5"
    },
    "retell": {
        "url": "https://api.retellai.com/create-agent",
        "api_key": "key_bb1af351c3b5ebde0fa18ee83e84"
    }
}


class AgentRequest(BaseModel):
    name: str
    description: Optional[str] = None
    language: str
    phone_number: Optional[str] = None
    provider: str

@app.post("/create-agent")
async def create_agent(request: AgentRequest):
    provider_config = CONFIG.get(request.provider)
    if not provider_config:
        raise HTTPException(status_code=400, detail="Invalid provider")

  
    if request.provider == "vapi":
        payload = {
            "name": request.name,
            "language": request.language
        }
    elif request.provider == "retell":
        payload = {
            "agent_name": request.name,
            "response_engine": {
                "type": "retell-llm",
                "llm_id": "llm_234sdertfsdsfsdf"
            },
            "voice_id": "11labs-Adrian",
            "version": 0
        }

    headers = {"Authorization": f"Bearer {provider_config['api_key']}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(provider_config["url"], json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {"status": "success", "data": response.json()}