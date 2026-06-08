from fastapi import FastAPI, HTTPException
from langchain_core.messages import HumanMessage
from app.schemas import TravelPlanRequest, TravelPlanResponse
from app.agent.graph import agent_graph

app = FastAPI(title="Global Guide - AI Agent Travel Planner")

@app.post("/plan", response_model=TravelPlanResponse)
async def create_travel_plan(request: TravelPlanRequest):
    try:
        initial_state = {"messages": [HumanMessage(content=request.query)]}
        result = await agent_graph.ainvoke(initial_state)
        
        formatted_messages = []
        for msg in result["messages"]:
            formatted_messages.append({
                "role": msg.type,
                "content": msg.content
            })
            
        return TravelPlanResponse(status="success", messages=formatted_messages)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}