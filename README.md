Global Guide Agent

Multi-step autonomous AI travel planning agent using LangGraph, Groq LLM, and FastAPI to execute tool calls without human intervention.

Architecture

Client → FastAPI → LangGraph State Machine → Groq LLM ↓ Tools (Weather, Places, Exchange Rate)

Setup

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key" > .env
docker build -t global-guide-agent .
uvicorn app.main:app --reload

Run

curl http://localhost:8000/health

curl -X POST http://localhost:8000/plan

-H "Content-Type: application/json"

-d '{"query": "Plan a trip to Tokyo", "user_id": "123"}' | python -m json.tool

Components

LangGraph: Workflow execution, tool definitions, and state management.
Groq LLM: Llama 3 for low-latency reasoning and Pydantic-validated tool calling.
Tools: OpenWeatherMap, Google Places, and Exchange Rate functions.
FastAPI: REST interface handling end-to-end request lifecycle and error recovery.
