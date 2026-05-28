from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer: str = Field(description="The agent's answer to the user's question")
    sources: List[Source] = Field(
        default_factory=list,
        description="List of sources used to generate the answer",
    )


def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
