# RAG Multiple Databases

## Features

- **Multi-source RAG**: Query multiple vector databases containing different types of documents
- **Swiss Airline Policy**: Access airline policy documents for customer service queries
- **Stories Database**: Search through fictional stories and narrative content
- **Web Search Integration**: Real-time web search capabilities using Tavily API
- **Intelligent Agent**: LangGraph-powered agent that can decide which tools to use based on query context
- **Chat Memory**: Persistent conversation history and memory management

## Architecture

The application uses:
- **LangGraph** for agent orchestration and decision-making
- **ChromaDB** for vector storage and similarity search
- **OpenAI** for embeddings and language model inference
- **Gradio** for the web interface
- **Tavily API** for web search capabilities

## Project Structure

```
RAG-multiple-databases/
├── src/
│   ├── app.py                      # Main Gradio application
│   ├── config.py                   # Configuration settings
│   ├── create_vector_db.py         # Vector database creation
│   ├── sample_questions.txt        # Example queries
│   ├── agent_graph/               # Agent and tools
│   │   ├── build_full_graph.py    # Main agent graph
│   │   ├── agent_backend.py       # Agent core logic
│   │   ├── tool_lookup_policy_rag.py  # Policy RAG tool
│   │   ├── tool_stories_rag.py    # Stories RAG tool
│   │   ├── tool_tavily_search.py  # Web search tool
│   │   └── load_tools_config.py   # Tools configuration
│   ├── chatbot/                   # Chatbot backend
│   │   ├── backend.py             # Chat logic
│   │   ├── memory.py              # Memory management
│   │   └── load_config.py         # Config loader
│   └── utils/                     # Utility functions
├── configs/
│   ├── project_config.yml         # Project settings
│   └── tools_config.yml           # Tools configuration
├── data/
│   ├── unstructured_docs/         # Source documents
│   │   ├── swiss_airline_policy/  # Airline policy PDFs
│   │   └── stories/               # Story documents
│   ├── airline_policy_vectordb/   # Policy vector DB
│   └── stories_vectordb/          # Stories vector DB
├── memory/                        # Chat history
└── images/                        # UI assets
```

## Environment Setup

### Prerequisites
- Python 3.12 or later
- uv package manager
- OpenAI API key
- Tavily API key (for web search)
- LangChain API key (optional, for tracing)

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```bash
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional for tracing
```

### Installation

1. Clone the repository and change directory:
   ```bash
   git clone https://github.com/thepatt/RAG-system-05-AI.git
   cd RAG-system-05-AI
   ```

2. Create and activate a virtual environment:
     ```bash
     uv init
     uv venv
     ```

3. Activate environment:
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. Install project dependencies using uv:
   ```bash
   uv sync
   ```

5. Create vector databases (run this once):
   ```bash
   uv run src/create_vector_db.py
   ```

6. Run the application:
   ```bash
   uv run src/app.py
   ```

7. Open your browser and navigate to the displayed local URL (typically `http://127.0.0.1:7860`)

## Usage

### Sample Queries

The application can handle various types of queries:

1. **Story-related questions**:
   - "In the stories, who is lily?"
   - "In the stories, who is fred?"

2. **Airline policy questions**:
   - "Based on the airline policy, do I need to reconfirm my flight?"
   - "Based on the airline policy, can I cancel my ticket 10 hours before the flight?"
   - "How can I change my booking?"

3. **General web search**:
   - "Who is the 47th president of USA?"

### How It Works

1. **Query Processing**: The agent receives your question through the Gradio interface
2. **Tool Selection**: Based on the query content, the agent decides which tool(s) to use:
   - Swiss Airline Policy RAG for policy-related questions
   - Stories RAG for narrative/story questions
   - Tavily Search for general web queries
3. **Information Retrieval**: The selected tool(s) retrieve relevant information
4. **Response Generation**: The agent synthesizes the information and provides a comprehensive answer
5. **Memory Storage**: The conversation is stored for future reference

## Configuration

### Project Configuration (`configs/project_config.yml`)
- LangSmith tracing settings
- Memory directory configuration

### Tools Configuration (`configs/tools_config.yml`)
- LLM model settings (GPT-4o-mini)
- Embedding model configuration
- Vector database parameters
- Search result limits
- Chunk sizes and overlaps

## Vector Databases

The application uses two main vector databases:

1. **Swiss Airline Policy Database**:
   - Contains airline policy documents (PDFs)
   - Used for customer service queries
   - Collection: `swiss-rag-chroma`

2. **Stories Database**:
   - Contains fictional stories and narratives
   - Used for story-related queries
   - Collection: `stories-rag-chroma`

## Development

### Adding New Tools

1. Create a new tool file in `src/agent_graph/`
2. Define the tool function with the `@tool` decorator
3. Add the tool to the graph in `build_full_graph.py`
4. Update the configuration files as needed

### Adding New Vector Databases

1. Add document sources to `data/unstructured_docs/`
2. Configure the new database in `tools_config.yml`
3. Update `create_vector_db.py` to include the new database
4. Create a corresponding RAG tool

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all required API keys are properly set in the `.env` file
2. **Vector Database Issues**: Run the vector database creation script again
3. **Memory Issues**: Check if the `memory/` directory exists and is writable
4. **Port Conflicts**: Gradio will automatically find an available port if 7860 is occupied

### Logs and Debugging

- The application prints detailed logs to the console
- LangSmith tracing can be enabled for detailed execution traces
- Vector database statistics are displayed during startup

## Dependencies

Key dependencies include:
- `langchain-openai`: OpenAI integration
- `langgraph`: Agent framework
- `chromadb`: Vector database
- `gradio`: Web interface
- `tavily-python`: Web search API

See `pyproject.toml` for the complete list of dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For questions or issues, please:
1. Check the troubleshooting section
2. Review the sample questions and usage examples
3. Open an issue on the repository

## Authors
- [Patrick aka Tai Mai](https://github.com/thepatt)