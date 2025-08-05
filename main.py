import os
from dotenv import load_dotenv
import asyncio
import json
from pprint import pprint
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

os.environ["GOOGLE_API_KEY"]
GITHUB_PERSONAL_ACCESS_TOKEN = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]


# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

async def main():
    # Set up the MultiServerMCPClient with your GitHub credentials
    client = MultiServerMCPClient(
        {
            "github": {
                "command": "/opt/homebrew/bin/npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-github"
                ],
                "env": {
                    "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_PERSONAL_ACCESS_TOKEN
                },
                "transport": "stdio"
            }
        }
    )

    # Get available tools
    tools = await client.get_tools()

    # Create the React agent with the tools
    agent = create_react_agent(llm, tools)

    
    query = "analyze catalogfi organization github and give me what they do and kind of repos they have"

    git_response = await agent.ainvoke({
        "messages": f"First, please call the context tool to get information about the current GitHub user and context. Then {query} "},
        {"recursion_limit": 100}
    )

    pprint(git_response)

if __name__ == "__main__":
    # Run the main async function
    asyncio.run(main())
