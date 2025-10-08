from agents import Agent, Runner, function_tool, ModelSettings
from dotenv import load_dotenv
import asyncio


@function_tool
def get_weather(city: str) -> str:
    """returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


async def main():
    agent = Agent(
        name="Weather Agent",
        instructions="Retrieve weather details.",
        tools=[get_weather],
        # You can force tool use by setting ModelSettings.tool_choice. Valid values are:
        # auto, which allows the LLM to decide whether or not to use a tool.
        # required, which requires the LLM to use a tool (but it can intelligently decide which tool).
        # none, which requires the LLM to not use a tool.
        # Setting a specific string e.g. get_weather, which requires the LLM to use that specific tool.
        model_settings=ModelSettings(tool_choice="get_weather"),
    )
    result = await Runner.run(agent, "Tell me about the weather in NYC.")
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
