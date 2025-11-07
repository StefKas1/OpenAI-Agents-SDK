from agents import Agent, Runner, SQLiteSession
import asyncio
from dotenv import load_dotenv

agent = Agent(name="Assistant")

# Different sessions maintain separate conversation histories
session_1 = SQLiteSession("user_123", "conversations.db")
session_2 = SQLiteSession("user_456", "conversations.db")


async def main():
    result1 = await Runner.run(agent, "Help me with my account", session=session_1)
    print(result1.final_output)

    result2 = await Runner.run(agent, "What are my charges?", session=session_2)
    print(result2.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
