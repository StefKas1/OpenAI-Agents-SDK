from agents import Agent, SQLiteSession
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

session = SQLiteSession("user_123", "conversations.db")


async def main():
    # Get all items in a session
    items = await session.get_items()
    print(items)

    # Add new items to a session
    new_items = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    await session.add_items(new_items)

    # Remove and return the most recent item
    last_item = await session.pop_item()
    print(last_item)  # {"role": "assistant", "content": "Hi there!"}

    # Clear all items from a session
    await session.clear_session()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
