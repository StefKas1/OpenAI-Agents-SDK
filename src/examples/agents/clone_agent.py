# save as agents_example.py
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool


@function_tool
def get_weather(city: str) -> str:
    """Simple tool that returns weather for a city."""
    return f"The weather in {city} is sunny."


async def main():
    pirate_agent = Agent(
        name="Pirate",
        instructions="Write like a pirate: short, salty replies (use 'Arrr', 'matey').",
        model="gpt-4",
        tools=[get_weather],
    )

    # Clone agent and change instructions
    robot_agent = pirate_agent.clone(
        name="Robot",
        instructions="Write like a robot: concise, factual, mechanical.",
        # optional: override tools if you don't want the same tools copied
        # tools=[],
    )

    pirate_result = await Runner.run(pirate_agent, "What's the weather in NYC?")
    print("Pirate final output:", pirate_result.final_output)

    robot_result = await Runner.run(robot_agent, "What's the weather in NYC?")
    print("Robot final output:", robot_result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
