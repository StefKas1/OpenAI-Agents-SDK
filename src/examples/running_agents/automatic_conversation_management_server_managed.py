import asyncio

from agents import Agent, Runner
from dotenv import load_dotenv


from openai import AsyncOpenAI


async def main():
    # Create a server-managed conversation
    conversation = await client.conversations.create()
    conv_id = conversation.id

    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # First turn
    result1 = await Runner.run(
        agent, "What city is the Golden Gate Bridge in?", conversation_id=conv_id
    )
    print(result1.final_output)
    # San Francisco

    # Second turn reuses the same conversation_id
    result2 = await Runner.run(
        agent,
        "What state is it in?",
        conversation_id=conv_id,
    )
    print(result2.final_output)
    # California


if __name__ == "__main__":
    load_dotenv()
    client = AsyncOpenAI()
    asyncio.run(main())
