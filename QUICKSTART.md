# VEXA Quick Start Guide

## 🚀 Immediate Demo (No Setup Required)

Test VEXA functionality right now without any setup:

```bash
python demo.py
```

This runs a demo mode that shows all VEXA capabilities without requiring Ollama.

## ⚡ Full Setup (5 Minutes)

### Option 1: Automated Setup

```bash
python setup.py
```

This will:
- Check dependencies
- Install required packages
- Verify Ollama installation
- Download default model
- Run tests

### Option 2: Manual Setup

1. **Install Ollama**:
   - Visit: https://ollama.ai/
   - Download and install for your OS

2. **Start Ollama**:
   ```bash
   ollama serve
   ```

3. **Install a model**:
   ```bash
   ollama pull mistral
   ```

4. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage Options

### Command Line Interface

```bash
# Interactive mode
python app/run_agent.py

# Single query
python app/run_agent.py --query "What's 2+2?"

# Different model
python app/run_agent.py --model llama2

# Show tools
python app/run_agent.py --tools-info
```

### Web Interface

```bash
# Start web UI
python ui/web_ui.py

# Custom port
python ui/web_ui.py --port 8080

# Public sharing
python ui/web_ui.py --share
```

### Python Integration

```python
from agent import create_vexa_agent

agent = create_vexa_agent()
response = agent.query("Hello!")
print(response["response"])
```

## 🎯 Example Queries

Try these queries to see VEXA in action:

- **Math**: "Calculate 15 * 23 + 100"
- **Time**: "What's the current date and time?"  
- **Search**: "Find latest AI news"
- **Files**: "List files in current directory"
- **General**: "Explain quantum computing"

## 🔧 Troubleshooting

### Common Issues

1. **Connection refused**:
   ```bash
   ollama serve  # Start Ollama first
   ```

2. **Model not found**:
   ```bash
   ollama pull mistral  # Install model
   ```

3. **Import errors**:
   ```bash
   pip install -r requirements.txt  # Install dependencies
   ```

## 📁 Project Structure

```
vexa/
├── 🎮 demo.py              # Try this first!
├── 🔧 setup.py             # Automated setup
├── 📖 README.md            # Full documentation
├── 📋 requirements.txt     # Dependencies
├── agent/                  # Core agent code
├── app/run_agent.py        # CLI interface
├── ui/web_ui.py           # Web interface
└── ai_agent.py            # Legacy simple version
```

## 🎉 Success Indicators

You'll know VEXA is working when you see:
- ✅ Agent initialized with model: mistral
- 🤖 VEXA: [intelligent responses]
- Tools being used automatically
- Fast, accurate responses

---

**🎮 Start with `python demo.py` to see VEXA in action immediately!**
