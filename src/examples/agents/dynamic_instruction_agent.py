from agents import Agent, Runner, RunContextWrapper
from dotenv import load_dotenv
import asyncio


class UserContext:
    def __init__(self, name: str):
        self.name = name


# Define dynamic instructions that depend on the user context
def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    return f"The user's name is {context.context.name}. Help them with their questions."


agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)


async def main():
    user_context = UserContext(name="Alice")
    result = await Runner.run(agent, "Hi there!", context=user_context)
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
