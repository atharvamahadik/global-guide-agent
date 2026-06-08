from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from app.config import settings
from app.agent.state import AgentState
from app.agent.tools import tools

model = ChatGroq(
    temperature=0, 
    model_name="llama3-70b-8192", 
    groq_api_key=settings.GROQ_API_KEY
)
model_with_tools = model.bind_tools(tools)

def call_model(state: AgentState):
    messages = state['messages']
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state: AgentState):
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

tool_node = ToolNode(tools)

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
workflow.add_edge("tools", "agent")

agent_graph = workflow.compile()