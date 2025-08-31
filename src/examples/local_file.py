import asyncio
import base64
import os

from agents import Agent, Runner
from dotenv import load_dotenv


FILEPATH = os.path.join(os.getcwd(), "media", "o3-and-o4-mini-system-card.pdf")


def file_to_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )

    b64_file = file_to_base64(FILEPATH)
    result = await Runner.run(
        agent,
        [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_data": f"data:application/pdf;base64,{b64_file}",
                        "filename": "o3-and-o4-mini-system-card.pdf",
                    }
                ],
            },
            {
                "role": "user",
                "content": "What is the first sentence of the introduction?",
            },
        ],
    )
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
