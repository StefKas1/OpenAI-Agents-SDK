from agents import Agent, Runner, SQLiteSession
import asyncio
from dotenv import load_dotenv

agent = Agent(name="Assistant")

# Different agents can share the same session
support_agent = Agent(name="Support")
billing_agent = Agent(name="Billing")
session = SQLiteSession("user_123")


async def main():
    result1 = await Runner.run(agent, "Help me with my account", session=session)
    print(result1.final_output)

    result2 = await Runner.run(agent, "What are my charges?", session=session)
    print(result2.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
