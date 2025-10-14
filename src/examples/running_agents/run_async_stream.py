import asyncio

from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv


async def main():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = Runner.run_streamed(agent, "Write a haiku about recursion in programming.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
