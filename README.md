# VEXA AI Agent

🤖 **VEXA** is a powerful, privacy-focused, and fully offline-capable AI Agent designed to perform intelligent tasks such as answering queries, searching the web, and using custom tools. Built using LangChain, Ollama, and DuckDuckGo, it utilizes open-source LLMs (like Mistral, LLaMA 2) to replicate ChatGPT-like functionality – without internet dependency, without API keys, and 100% free.

## 💡 Key Features

✅ **Runs Locally**: Uses open-source LLMs via Ollama — no need for paid APIs  
🔍 **Web Search Tool**: Integrated with DuckDuckGo for real-time answers and current events  
🤖 **LangChain Agent**: Powered by the ReAct Agent with tool chaining  
🖥️ **Command-line & Web UI**: Interact via terminal or simple Gradio interface  
🔧 **Modular & Scalable**: Easily plug in your own tools (PDF reader, calculator, etc.)  
🔒 **Private & Offline-Ready**: Great for local development and secure environments  

## 🧱 Tech Stack

| Layer | Tool |
|-------|------|
| 💬 **LLM** | Ollama – Mistral / LLaMA 2 |
| 🤖 **Agent Framework** | LangChain |
| 🌐 **Search Tool** | DuckDuckGo Search API |
| ⚙️ **Programming** | Python |
| 🌐 **Optional UI** | Gradio |

## 🧪 How It Works

1. **Ollama** loads a local LLM (e.g., `mistral`) to serve as the brain of the agent
2. **LangChain** initializes an agent with custom tools like DuckDuckGo search
3. The user inputs a question via terminal or web UI
4. The agent decides whether to:
   - Answer directly using the LLM, or
   - Use a tool like search, then respond
5. Output is returned intelligently, step-by-step

## 📁 Project Structure

```
vexa/
├── agent/
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Model and configuration settings
│   ├── core.py            # Agent logic using LangChain
│   └── tools.py           # Tools like DuckDuckGo, calculator, etc.
├── app/
│   └── run_agent.py       # CLI runner
├── ui/
│   └── web_ui.py          # Gradio web interface (optional)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── ai_agent.py           # Original simple version (legacy)
```

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**:
   ```bash
   # Visit https://ollama.ai/ or install via:
   # Windows: Download from website
   # macOS: brew install ollama
   # Linux: curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull a model**:
   ```bash
   ollama pull mistral
   # or
   ollama pull llama2
   ```

3. **Start Ollama server**:
   ```bash
   ollama serve
   ```

### Installation

1. **Clone/Download the project**:
   ```bash
   git clone <repository-url>
   cd vexa
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage Options

#### Option 1: Command Line Interface

```bash
# Basic usage with default model (mistral)
python app/run_agent.py

# Use specific model
python app/run_agent.py --model llama2

# Single query mode
python app/run_agent.py --query "What's the weather like today?"

# Show available tools
python app/run_agent.py --tools-info

# Verbose mode for debugging
python app/run_agent.py --verbose
```

#### Option 2: Web Interface (Gradio)

```bash
# Launch web UI with default settings
python ui/web_ui.py

# Custom port and model
python ui/web_ui.py --model llama2 --port 8080

# Share publicly (creates public link)
python ui/web_ui.py --share
```

Then open your browser to `http://localhost:7860` (or specified port).

#### Option 3: Python Integration

```python
from agent import create_vexa_agent

# Create agent instance
agent = create_vexa_agent(model_name="mistral")

# Ask questions
response = agent.query("What's the current date?")
print(response["response"])

# Search the web
response = agent.query("Latest AI news 2024")
print(response["response"])
```

## 🛠️ Available Tools

- **🔍 Web Search**: Search the web using DuckDuckGo
- **🧮 Calculator**: Perform mathematical calculations
- **📅 DateTime**: Get current date and time information  
- **📁 File Operations**: Basic file system operations
- **🌤️ Weather**: Weather information (placeholder for demo)

## 💬 Example Interactions

```
🤔 Ask me anything: What's 15 * 23?
🤖 VEXA: I'll calculate that for you.
Result: 345

🤔 Ask me anything: What's the latest news about AI?
🤖 VEXA: Let me search for the latest AI news...
[Searches web and provides current information]

🤔 Ask me anything: What time is it?
🤖 VEXA: Current date and time: 2024-08-08 14:30:25
```

## 🔧 Customization

### Adding Custom Tools

Create your custom tool:

```python
from langchain_core.tools import Tool

def my_custom_function(input_text: str) -> str:
    return f"Processed: {input_text}"

custom_tool = Tool(
    name="my_tool",
    func=my_custom_function,
    description="Description of what this tool does"
)

# Add to agent
agent.add_tool(custom_tool)
```

### Configuration

Edit `agent/config.py` to modify:
- Default models
- Agent settings
- UI configuration
- Tool parameters

## 🚨 Troubleshooting

### Common Issues

1. **"Failed to initialize agent"**:
   - Ensure Ollama is running: `ollama serve`
   - Check if model is installed: `ollama list`
   - Install required model: `ollama pull mistral`

2. **"Model not found"**:
   - Use `python app/run_agent.py --models` to see available models
   - Pull the model: `ollama pull <model-name>`

3. **Web search not working**:
   - Check internet connection
   - DuckDuckGo might have rate limits

4. **Web UI not loading**:
   - Install gradio: `pip install gradio>=4.0.0`
   - Check if port is available
   - Try a different port: `--port 8080`

### Performance Tips

- **For faster responses**: Use smaller models like `mistral` or `orca-mini`
- **For better quality**: Use larger models like `llama2` or `llama3`
- **For coding tasks**: Use `codellama` model

## 🚀 Use Cases

- 👨‍💻 **Personal productivity assistant**
- 🧑‍🏫 **Study buddy for offline environments**  
- 🔒 **Secure AI assistant for private organizations**
- 🧪 **Testing LangChain agent logic without paid APIs**
- 🌐 **Local chatbot with web search capabilities**
- 📊 **Data analysis and calculations**

## 🔒 Privacy & Security

- **100% Local Processing**: All queries processed on your machine
- **No Data Collection**: No telemetry or data sent to external servers
- **Offline Capable**: Works without internet (except for web search)
- **Open Source**: Full transparency of code and models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source. See LICENSE file for details.

## 🙏 Acknowledgments

- **Ollama** for local LLM serving
- **LangChain** for agent framework
- **DuckDuckGo** for search capabilities
- **Gradio** for web interface
- **Open Source LLM Community** for the models

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Verify Ollama is running with the correct model
4. Check GitHub issues for similar problems

---

**Made with ❤️ for the open-source AI community**
