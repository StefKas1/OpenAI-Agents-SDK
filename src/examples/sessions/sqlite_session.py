from agents import Agent, Runner, SQLiteSession
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

# Create a session instance with a session ID
session = SQLiteSession("conversation_123")


async def main():
    # First turn
    result = await Runner.run(
        agent, "What city is the Golden Gate Bridge in?", session=session
    )
    print(result.final_output)  # "San Francisco"

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(agent, "What state is it in?", session=session)
    print(result.final_output)  # "California"


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
