from agents import Agent, Runner, SQLiteSession
import asyncio
from dotenv import load_dotenv

load_dotenv()

agent = Agent(name="Assistant")
session = SQLiteSession("correction_example")


async def main():
    # Initial conversation
    result = await Runner.run(agent, "What's 2 + 2?", session=session)
    print(f"Agent: {result.final_output}")

    # User wants to correct their question
    assistant_item = await session.pop_item()  # Remove agent's response
    user_item = await session.pop_item()  # Remove user's question

    # Ask a corrected question
    result = await Runner.run(agent, "What's 2 + 3?", session=session)
    print(f"Agent: {result.final_output}")


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
