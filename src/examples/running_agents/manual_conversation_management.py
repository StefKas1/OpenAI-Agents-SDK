import asyncio

from agents import Agent, Runner, trace
from dotenv import load_dotenv


async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    thread_id = "thread_123"  # Example thread ID
    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(agent, "What city is the Golden Gate Bridge in?")
        print(result.final_output)
        # San Francisco

        # Second turn
        new_input = result.to_input_list() + [
            {"role": "user", "content": "What state is it in?"}
        ]
        result = await Runner.run(agent, new_input)
        print(result.final_output)
        # California


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
