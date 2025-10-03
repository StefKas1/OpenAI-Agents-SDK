from agents import Agent, Runner
from dotenv import load_dotenv
# Define the specialist agents

booking_agent = Agent(
    name="Booking Agent",
    instructions=(
        "You handle booking-related questions from the user. "
        "If the user asks about making or managing a booking, do so. "
        "If the user asks about refunds or cancellation, you can refuse and defer."
    ),
)

refund_agent = Agent(
    name="Refund Agent",
    instructions=(
        "You handle refund-related questions from the user. "
        "If the user asks about refund policy or processing a refund, respond. "
        "If the user asks about booking new items, refuse and defer."
    ),
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a triage agent whose job is to route the user's request to the correct specialist. "
        "If the user is asking about booking (making, changing, new reservation), hand off to the Booking Agent. "
        "If the user is asking about refunds, cancellations, or refund policy, hand off to the Refund Agent. "
        "If it’s unclear, ask a clarifying question to decide which specialist should handle it."
    ),
    handoffs=[booking_agent, refund_agent],
)


def run_example_sync(user_input: str):
    result = Runner.run_sync(triage_agent, user_input)
    print("Final output:", result.final_output)


if __name__ == "__main__":
    load_dotenv()
    run_example_sync("I want to book a flight from Berlin to Paris next week.")
    run_example_sync("How do I get a refund for my cancelled reservation?")
    run_example_sync("I changed my mind — can you help me?")
