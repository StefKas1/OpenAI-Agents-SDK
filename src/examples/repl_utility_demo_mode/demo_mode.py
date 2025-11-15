import asyncio
from agents import Agent, run_demo_loop
from dotenv import load_dotenv

load_dotenv()


# run_demo_loop for quick, interactive testing of an agent's behavior directly in your terminal
async def main() -> None:
    agent = Agent(name="Assistant", instructions="You are a helpful assistant.")
    await run_demo_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())
