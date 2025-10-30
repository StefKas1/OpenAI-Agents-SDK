from agents import Agent, Runner, OpenAIConversationsSession
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

# Create a new conversation
session = OpenAIConversationsSession()

# Optionally resume a previous conversation by passing a conversation ID
# session = OpenAIConversationsSession(conversation_id="conv_123")


async def main():
    # Start conversation
    result = await Runner.run(
        agent, "What city is the Golden Gate Bridge in?", session=session
    )
    print(result.final_output)  # "San Francisco"

    # Continue the conversation
    result = await Runner.run(agent, "What state is it in?", session=session)
    print(result.final_output)  # "California"


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
