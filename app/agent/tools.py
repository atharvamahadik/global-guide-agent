from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Fetch current weather for a specific location."""
    return f"The current weather in {location} is 22°C and sunny."

@tool
def search_places(query: str, location: str) -> str:
    """Search for places or attractions in a given location."""
    return f"Top results for '{query}' in {location}: 1. Central Park, 2. Local Market."

@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """Get the current currency exchange rate."""
    return f"1 {base_currency} is equal to 0.92 {target_currency}."

tools = [get_weather, search_places, get_exchange_rate]