from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from conversation_agent import RoadmapConversationAgent
from dynamic_llm_conversation_agent import DynamicLLMConversationAgent
import os
from fastapi.staticfiles import StaticFiles
# Ensure the output directory exists at startup
os.makedirs("output", exist_ok=True)

app = FastAPI()

app.mount("/output", StaticFiles(directory="output"), name="output")
# agent = RoadmapConversationAgent()  # Single global agent
openai_api_key = os.getenv("OPENAI_API_KEY")  # Make sure your key is in your .env or environment

# Store agents by session_id
agents = {}

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://polite-river-0cb7dce00.1.azurestaticapps.net"],  # In production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session store (for demo; use Redis or DB for production)


class ConversationInput(BaseModel):
    user_input: str
    session_id: str

@app.post("/api/conversation")
async def conversation(input: ConversationInput):
    agent = agents.get(input.session_id)
    if not agent:
        agent = DynamicLLMConversationAgent(openai_api_key=openai_api_key)
        agents[input.session_id] = agent
    result = agent.handle_user_input(input.user_input)
    
    return result