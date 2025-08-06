# GitHub MCP Analyzer

A Python application that leverages the Model Context Protocol (MCP) to analyze GitHub organizations using Google's Gemini AI model. This tool can fetch and analyze repository information, organization structure, and provide insights about GitHub organizations.

## Features

- 🔍 **Organization Analysis**: Analyze any GitHub organization's repositories and structure
- 🤖 **AI-Powered Insights**: Uses Google Gemini 2.5 Flash model for intelligent analysis
- 🔧 **MCP Integration**: Leverages Model Context Protocol for seamless GitHub API interaction
- 📊 **Comprehensive Reports**: Get detailed information about repositories, technologies used, and organization overview

## Prerequisites

- Python 3.11 or higher
- Node.js and npm (for MCP GitHub server)
- GitHub Personal Access Token
- Google AI API Key

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd github-mcp
```

2. **Install Python dependencies**
```bash
pip install uv 
```

```bash
uv sync
```

3. **Install Node.js dependencies** (for MCP GitHub server)
```bash
npm install -g @modelcontextprotocol/server-github
```

## Configuration

1. **Create a `.env` file** in the project root:
```env
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token_here
GOOGLE_API_KEY=your_google_ai_api_key_here
```

2. **Get a GitHub Personal Access Token**:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate a new token with appropriate repository permissions
   - Copy the token to your `.env` file

3. **Get a Google AI API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create an API key
   - Copy the key to your `.env` file

## Usage

### Basic Usage

Run the main script to analyze a GitHub organization:

```python
uv run main.py
```

The current example analyzes the "catalogfi" organization, but you can modify the query in the code:

```python
query = "analyze [organization-name] github and give me what they do and kind of repos they have"
```

### Customizing Analysis

You can modify the analysis query to focus on specific aspects:

```python
# Examples of different queries
query = "analyze microsoft organization and focus on machine learning repositories"
query = "give me statistics about facebook organization's programming languages usage"
query = "analyze google organization and list their most popular repositories"
```

## Code Structure

```
github-mcp/
├── main.py              # Main application script
├── pyproject.toml       # Project configuration and dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Key Components

- **MultiServerMCPClient**: Manages MCP server connections for GitHub integration
- **ChatGoogleGenerativeAI**: Google Gemini model for AI analysis
- **create_react_agent**: LangChain agent that can reason and use tools
- **GitHub MCP Server**: Provides GitHub API access through MCP protocol

## Example Output

The tool provides detailed analysis including:
- Organization overview and mission
- Repository categories and technologies used
- Popular repositories and their purposes
- Development patterns and statistics
- Technology stack analysis

## Dependencies

### Core Dependencies
- `langchain`: LangChain framework for LLM applications
- `langchain-google-genai`: Google Gemini integration
- `langgraph`: Graph-based agent framework
- `langchain-mcp-adapters`: MCP protocol adapters
- `python-dotenv`: Environment variable management

### MCP Server
- `@modelcontextprotocol/server-github`: GitHub MCP server (npm package)

## Troubleshooting

### Common Issues

1. **GitHub Token Permissions**
   - Ensure your token has sufficient permissions to read organization and repository data
   - For private repositories, additional permissions may be required

2. **Google AI API Limits**
   - Check your API quota and billing settings
   - Consider rate limiting for large organizations

3. **Node.js/npm Issues**
   - Ensure Node.js is properly installed and accessible
   - Verify the MCP GitHub server is installed globally: `npm list -g @modelcontextprotocol/server-github`

4. **Environment Variables**
   - Double-check your `.env` file formatting
   - Ensure no extra spaces or quotes around values

## Configuration Options

### Adjusting Recursion Limit
```python
git_response = await agent.ainvoke({
    "messages": f"First, please call the context tool to get information about the current GitHub user and context. Then {query}"
}, {"recursion_limit": 100})  # Increase for complex analyses
```

### Changing AI Model
```python
# Use different Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```