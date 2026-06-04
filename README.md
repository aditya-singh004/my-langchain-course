# LangChain ReAct Search Agent

A small LangChain project that builds a search-enabled agent with OpenAI and Tavily. The agent asks a current-events question, searches the web, and returns a structured response with an answer and source URLs.

## What It Does

- Loads API keys from a local `.env` file.
- Uses `ChatOpenAI` as the language model.
- Uses Tavily search as the external search tool.
- Defines a structured response schema with Pydantic.
- Runs a sample query from `main.py`.

## Project Structure

```text
.
|-- main.py
|-- pyproject.toml
|-- uv.lock
|-- README.md
`-- .gitignore
```

## Requirements

- Python 3.14 or newer
- OpenAI API key
- Tavily API key
- `uv` for dependency management

## Setup

Clone the repository:

```powershell
git clone https://github.com/aditya-singh004/my-langchain-course.git
cd my-langchain-course
```

Install dependencies:

```powershell
uv sync
```

If Tavily is not installed in your environment yet, add it before running the script:

```powershell
uv add langchain-tavily
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The `.env` file is ignored by Git, so your API keys stay local.

## Run

```powershell
uv run python main.py
```

The script currently runs this sample request:

```text
Search for the latest AI news published today.
```

## How It Works

`main.py` defines two Pydantic models:

- `Source`: stores a source URL used by the agent.
- `AgentResponse`: stores the final answer and a list of sources.

The agent is created with:

```python
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
```

This tells LangChain to use the OpenAI model, call Tavily when search is needed, and return output that follows the `AgentResponse` schema.

## Customize The Query

Edit the message inside `main.py`:

```python
result = agent.invoke({
    "messages": [HumanMessage(content="Your question here")]
})
```

Then run the script again.
