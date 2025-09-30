from agents import Agent, Runner
from pydantic import BaseModel
from dotenv import load_dotenv
import asyncio


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


async def main():
    agent = Agent(
        name="Calendar extractor",
        instructions="Extract calendar events from text",
        output_type=CalendarEvent,
    )
    result = await Runner.run(agent, "What is today's date?")
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
