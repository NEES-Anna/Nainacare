from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from model import generate_reply

# Initialize FastAPI
app = FastAPI(
    title="NainaCare API",
    description="API backend for NainaCare Wellness AI project",
    version="1.0.0"
)

# -----------------------------
# Input and Output Models
# -----------------------------
class ChatIn(BaseModel):
    text: str
    context: Optional[Dict] = None
    language: str = "en"

class ChatOut(BaseModel):
    reply: str
    sentiment: str
    safety: str

# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------
# Chat Endpoint
# -----------------------------
@app.post("/chat", response_model=ChatOut)
def chat(msg: ChatIn):
    if not msg.text.strip():
        raise HTTPException(status_code=400, detail="Empty text")

    # Stub for now: You can connect model.py logic here
    reply, sentiment, safety = generate_reply(msg.text, msg.language)

    return ChatOut(reply=reply, sentiment=sentiment, safety=safety)


# -----------------------------
# Helper Function (Mock)
# Replace with actual logic from model.py later
# -----------------------------
def generate_reply(text: str, lang: str):
    # Placeholder logic
    reply = f"You said: {text} (lang: {lang})"
    sentiment = "neutral"
    safety = "safe"
    return reply, sentiment, safety
