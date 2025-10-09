from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
import asyncio


@function_tool
def get_weather(city: str) -> str:
    """returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


async def main():
    agent = Agent(
        name="Weather agent",
        instructions="Retrieve weather details.",
        model="gpt-4",
        tools=[get_weather],
        tool_use_behavior="stop_on_first_tool",  # The output of the first tool call is used as the final response, without further LLM processing.
    )
    result = await Runner.run(agent, "Tell me about the weather in NYC.")
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
