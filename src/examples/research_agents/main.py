import asyncio

from src.examples.research_agents.manager import ResearchManager
from dotenv import load_dotenv

# Run: PYTHONPATH=. python src/examples/research_agents/main.py
# Or: python -m src.examples.research_agents.main

async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
