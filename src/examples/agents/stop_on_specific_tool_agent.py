from agents import Agent, Runner, function_tool
from agents.agent import StopAtTools
from dotenv import load_dotenv
import asyncio


@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


@function_tool
def sum_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


async def main():
    agent = Agent(
        name="Stop At Stock Agent",
        instructions="Get weather or sum numbers.",
        tools=[get_weather, sum_numbers],
        tool_use_behavior=StopAtTools(stop_at_tool_names=["get_weather"]),
    )
    result = await Runner.run(
        agent, "Tell me about the weather in NYC. And what is 2 + 2?"
    )
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
