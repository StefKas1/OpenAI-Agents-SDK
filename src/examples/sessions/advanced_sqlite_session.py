from agents import Agent, Runner
import asyncio
from agents.extensions.memory import AdvancedSQLiteSession
from dotenv import load_dotenv

load_dotenv()

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

# Create with advanced features
session = AdvancedSQLiteSession(
    session_id="user_123", db_path="conversations.db", create_tables=True
)


async def main():
    # Automatic usage tracking
    result = await Runner.run(agent, "Hello", session=session)
    await session.store_run_usage(result)  # Track token usage

    result = await Runner.run(agent, "How are you?", session=session)

    # Conversation branching
    await session.create_branch_from_turn(2)  # Branch from turn 2


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
