from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv

booking_agent = Agent(
    name="BookingAgent",
    instructions="You are the expert for bookings. Handle booking requests, availability checks, etc.",
)

refund_agent = Agent(
    name="RefundAgent",
    instructions="You are the expert for refunds. Handle refund requests, eligibility, etc.",
)

# Define the manager / orchestration / customer-facing agent that uses those as tools
customer_facing_agent = Agent(
    name="CustomerFacingAgent",
    instructions=(
        "You are the first interface with the user. "
        "If the user's intent involves bookings, call booking_expert. "
        "If it involves refunds, call refund_expert. "
        "Otherwise, respond directly."
    ),
    tools=[
        booking_agent.as_tool(
            tool_name="booking_expert",
            tool_description="Use this tool to answer booking-related questions",
        ),
        refund_agent.as_tool(
            tool_name="refund_expert",
            tool_description="Use this tool to answer refund-related questions",
        ),
    ],
)


# Example run
async def main():
    result = await Runner.run(
        customer_facing_agent, "I want to cancel and get a refund for my booking."
    )
    print("Final:", result.final_output)

    result2 = await Runner.run(
        customer_facing_agent, "Can you book me a flight from A to B?"
    )
    print("Final:", result2.final_output)

    result3 = await Runner.run(customer_facing_agent, "What's the weather today?")
    print("Final:", result3.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
