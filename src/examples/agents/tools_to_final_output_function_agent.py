from agents import Agent, Runner, function_tool, FunctionToolResult, RunContextWrapper
from agents.agent import ToolsToFinalOutputResult
from typing import List, Any
from dotenv import load_dotenv
import asyncio

load_dotenv()


@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


def custom_tool_handler(
    context: RunContextWrapper[Any], tool_results: List[FunctionToolResult]
) -> ToolsToFinalOutputResult:
    """Processes tool results to decide final output."""
    for result in tool_results:
        if result.output and "sunny" in result.output:
            return ToolsToFinalOutputResult(
                is_final_output=True, final_output=f"Final weather: {result.output}"
            )
    return ToolsToFinalOutputResult(is_final_output=False, final_output=None)


async def main():
    agent = Agent(
        name="Weather Agent",
        instructions="Retrieve weather details.",
        tools=[get_weather],
        tool_use_behavior=custom_tool_handler,
    )
    result = await Runner.run(agent, "Tell me about the weather in NYC.")
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
