# VEXA AI Agent

🤖 **VEXA** is a powerful, privacy-focused, and fully offline-capable AI Agent designed to perform intelligent tasks such as answering queries, searching the web, and using custom tools. Built using LangChain, Ollama, and DuckDuckGo, it utilizes open-source LLMs (like Mistral, LLaMA 2) to replicate ChatGPT-like functionality – without internet dependency, without API keys, and 100% free.

## 🚀 **Try VEXA Right Now!**

| 🎯 **Immediate Use** | 🤖 **Full AI Mode** |
|---------------------|---------------------|
| `python simple_vexa.py` | `python app/run_agent.py` |
| ✅ **Works now!** | ⚠️ **Requires Ollama** |
| Interactive chat | Advanced AI responses |
| Calculator, date/time, files | + Web search |
| No setup needed | Setup: Install Ollama |

**No setup required - works immediately:**

```bash
# Interactive AI assistant (works now!)
python simple_vexa.py

# Or see a demonstration  
python demo.py
```

**Features available immediately:**
- 🧮 **Calculator**: Solve math problems
- 📅 **Date/Time**: Current date and time info
- 📁 **File Operations**: List files and directories  
- 🤖 **Interactive Chat**: Real-time conversation interface
- 🔒 **100% Offline**: No internet or API keys needed

**For full AI capabilities with web search and advanced reasoning, install Ollama (see setup below).**

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
├── 🎮 demo.py              # Working demo (no Ollama required) ← START HERE!
├── 🖥️ simple_vexa.py       # Interactive mode (no Ollama) ← TRY THIS!
├── 🔧 setup.py             # Automated setup script
├── 📊 test_components.py   # Component testing
├── 📋 STATUS.md            # Current project status
├── 📖 README.md            # This documentation
├── ⚡ QUICKSTART.md        # Quick start guide
├── 📋 requirements.txt     # Python dependencies
├── 🔄 ai_agent.py          # Legacy simple version (requires Ollama)
├── agent/                  # 🧠 Core agent package
│   ├── __init__.py         # Package initialization
│   ├── config.py          # Model and configuration settings
│   ├── core.py            # Agent logic using LangChain
│   └── tools.py           # Tools like DuckDuckGo, calculator, etc.
├── app/                   # 🖥️ CLI applications
│   └── run_agent.py       # Full CLI interface (requires Ollama)
└── ui/                    # 🌐 Web interface
    └── web_ui.py          # Gradio web UI (requires Ollama)
```

## 🚀 Quick Start

### 🎯 **Immediate Usage (No Setup Required)**

**Try VEXA right now without installing anything!**

```bash
# Interactive VEXA - chat interface with real tools
python simple_vexa.py

# Or demo mode - automated demonstration
python demo.py

# Test all components
python test_components.py
```

These versions work immediately with:
- ✅ Real calculator functionality
- ✅ Date/time queries  
- ✅ File operations
- ✅ Interactive chat interface
- ✅ No dependencies on external services

### 🤖 **Full AI Experience (Requires Ollama)**

For the complete AI agent with LLM intelligence:

#### Prerequisites

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

#### Installation

1. **Clone/Download the project**:
   ```bash
   git clone <repository-url>
   cd vexa
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run automated setup** (optional):
   ```bash
   python setup.py
   ```

### Usage Options

#### ⚡ **Option 1: Immediate Usage (Recommended)**

**No setup required - works right now!**

```bash
# Interactive mode with real tools
python simple_vexa.py

# Demo with automated examples  
python demo.py

# Verify everything works
python test_components.py
```

**Features available immediately:**
- 🧮 Calculator: "calculate 2+2", "what's 15*23?"
- 📅 DateTime: "what time is it?", "current date"  
- 📁 File ops: "list files", "show directory"
- ❓ Help system: "help", "tools"

#### 🤖 **Option 2: Full AI Agent (Requires Ollama)**

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

#### 🌐 **Option 3: Web Interface (Requires Ollama + Gradio)**

```bash
# Launch web UI with default settings
python ui/web_ui.py

# Custom port and model
python ui/web_ui.py --model llama2 --port 8080

# Share publicly (creates public link)
python ui/web_ui.py --share
```

Then open your browser to `http://localhost:7860` (or specified port).

#### 💻 **Option 4: Python Integration**

```python
from agent import create_vexa_agent

# Create agent instance (requires Ollama)
agent = create_vexa_agent(model_name="mistral")

# Ask questions
response = agent.query("What's the current date?")
print(response["response"])

# Search the web
response = agent.query("Latest AI news 2025")
print(response["response"])
```

**Note**: Python integration requires Ollama to be running. For immediate usage without setup, use `python simple_vexa.py`.

## 🛠️ Available Tools

- **🔍 Web Search**: Search the web using DuckDuckGo
- **🧮 Calculator**: Perform mathematical calculations
- **📅 DateTime**: Get current date and time information  
- **📁 File Operations**: Basic file system operations
- **🌤️ Weather**: Weather information (placeholder for demo)

## 💬 Example Interactions

### **Simple Mode Examples** (Available Now)

```
🤔 Ask me anything: calculate 15 * 23
🤖 VEXA: Result: 345

🤔 Ask me anything: what time is it?
🤖 VEXA: Current time: 21:02:21

🤔 Ask me anything: list files
🤖 VEXA: Files in current directory: agent, demo.py, README.md, app, ui...

🤔 Ask me anything: help
🤖 VEXA: Available commands:
🧮 Calculator: "calculate 2+2", "what's 15*23?"
📅 DateTime: "what time is it?", "current date"
📁 Files: "list files", "show directory"
```

### **Full AI Mode Examples** (With Ollama)

```
🤔 Ask me anything: What's the latest news about AI?
🤖 VEXA: Let me search for the latest AI news...
[Uses DuckDuckGo to find and summarize current AI news]

🤔 Ask me anything: Explain quantum computing in simple terms
🤖 VEXA: Quantum computing is a revolutionary approach to computation...
[Provides detailed, intelligent explanation]

🤔 Ask me anything: What's the weather in New York?
🤖 VEXA: I'll search for current weather information in New York...
[Searches web and provides current weather data]
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

### **Quick Solutions**

#### 🎯 **Want to use VEXA right now?**
```bash
python simple_vexa.py    # Interactive mode - works immediately
python demo.py           # Demo mode - shows all features
```

#### ❓ **Connection issues with main app?**
The full AI agent needs Ollama running. Use simple mode instead!

### **Common Issues**

1. **"Failed to initialize agent"** / **"Connection refused"**:
   - **Quick Fix**: Use `python simple_vexa.py` (works without Ollama)
   - **Full Fix**: Ensure Ollama is running: `ollama serve`
   - Check if model is installed: `ollama list`
   - Install required model: `ollama pull mistral`

2. **"Model not found"**:
   - Use `python app/run_agent.py --models` to see available models
   - Pull the model: `ollama pull <model-name>`

3. **Import errors** / **Module not found**:
   - Install dependencies: `pip install -r requirements.txt`
   - Test components: `python test_components.py`

4. **Web search not working**:
   - Check internet connection
   - DuckDuckGo might have rate limits
   - Use simple mode for offline functionality

5. **Web UI not loading**:
   - Install gradio: `pip install gradio>=4.0.0`
   - Check if port is available
   - Try a different port: `--port 8080`

### **What Works When**

| Feature | Simple Mode | Full AI Mode |
|---------|-------------|--------------|
| Calculator | ✅ Works now | ✅ Needs Ollama |
| DateTime | ✅ Works now | ✅ Needs Ollama |
| File Operations | ✅ Works now | ✅ Needs Ollama |
| Interactive Chat | ✅ Works now | ✅ Needs Ollama |
| Web Search | ❌ | ✅ Needs Ollama |
| AI Responses | Basic | ✅ Needs Ollama |
| Web UI | ❌ | ✅ Needs Ollama |

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

1. **Try simple mode first**: `python simple_vexa.py` (works without any setup)
2. **Check component status**: `python test_components.py` 
3. **Read status report**: Check `STATUS.md` for current project status
4. **Ensure all dependencies are installed**: `pip install -r requirements.txt`
5. **For full AI features**: Verify Ollama is running with the correct model
6. **Check GitHub issues** for similar problems

## 🎯 **TL;DR - Just Want to Use VEXA?**

**Run this command right now:**
```bash
python simple_vexa.py
```

**You'll get:**
- ✅ Interactive AI assistant interface
- ✅ Working calculator, date/time, file operations
- ✅ No setup, no dependencies, no internet required
- ✅ Immediate functionality

**Want more features?** Install Ollama and use `python app/run_agent.py` for web search and advanced AI responses.

---

**Made with ❤️ for the open-source AI community**
