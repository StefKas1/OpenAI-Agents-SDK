from agents import Agent, Runner
from dotenv import load_dotenv


def main():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    # Runner.run(), which runs async and returns a RunResult.
    result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)
    # Code within the code,
    # Functions calling themselves,
    # Infinite loop's dance


if __name__ == "__main__":
    load_dotenv()
    main()
