import asyncio

from agents import Agent, Runner, trace, SQLiteSession
from dotenv import load_dotenv


async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create session instance
    session = SQLiteSession("conversation_123")

    thread_id = "thread_123"  # Example thread ID
    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(
            agent, "What city is the Golden Gate Bridge in?", session=session
        )
        print(result.final_output)
        # San Francisco

        # Second turn - agent automatically remembers previous context
        result = await Runner.run(agent, "What state is it in?", session=session)
        print(result.final_output)
        # California


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
