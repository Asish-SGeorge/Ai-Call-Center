from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai

from agents import PrimaryAgent
from supervisor import SupervisorAgent
from escalation import EscalationAgent
from memory import ConversationMemory

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-lite-latest")

app = FastAPI()

# ENABLE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

primary = PrimaryAgent(model)
supervisor = SupervisorAgent()
escalator = EscalationAgent()
memory = ConversationMemory()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    memory.add("User", req.message)
    context = memory.get_context()

    ai_response = primary.respond(req.message, context)
    memory.add("AI", ai_response)

    analysis = supervisor.analyze(req.message, ai_response)

    status = "resolved"
    if analysis["emotion"] == "angry" or analysis["confidence"] < 0.6:
        status = "escalated"

    return {
        "reply": ai_response,
        "analysis": {
            "status": status,
            "confidence": int(analysis["confidence"] * 100)
        }
    }

@app.get("/")
def root():
    return {"status": "Backend running"}
