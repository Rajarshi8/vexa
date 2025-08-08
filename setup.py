#!/usr/bin/env python3
"""
Setup and Installation Script for VEXA AI Agent

This script helps you set up VEXA with proper dependencies and configuration.
"""

import subprocess
import sys
import os
import platform


def run_command(command, description=""):
    """Run a system command and return success status"""
    if description:
        print(f"🔄 {description}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success: {description}")
            return True, result.stdout
        else:
            print(f"❌ Failed: {description}")
            print(f"Error: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        print(f"❌ Exception running command: {e}")
        return False, str(e)


def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is too old. Requires Python 3.8+")
        return False


def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    
    packages = [
        "langchain>=0.3.0",
        "langchain-core>=0.3.0", 
        "langchain-community>=0.3.0",
        "langchain-ollama>=0.2.0",
        "duckduckgo-search>=8.0.0",
        "gradio>=4.0.0",
        "requests>=2.31.0",
        "python-dateutil>=2.8.0"
    ]
    
    for package in packages:
        success, output = run_command(f"pip install {package}", f"Installing {package}")
        if not success:
            return False
    
    return True


def check_ollama():
    """Check if Ollama is installed and running"""
    print("🤖 Checking Ollama installation...")
    
    # Check if ollama command exists
    success, output = run_command("ollama --version", "Checking Ollama version")
    if not success:
        print("❌ Ollama is not installed or not in PATH")
        print("📥 Please install Ollama from: https://ollama.ai/")
        return False
    
    print(f"✅ Ollama found: {output.strip()}")
    
    # Check if ollama is running
    success, output = run_command("ollama list", "Checking available models")
    if not success:
        print("⚠️ Ollama might not be running. Start it with: ollama serve")
        return False
    
    print("✅ Ollama is running")
    print("📋 Available models:")
    print(output)
    
    return True


def install_default_model():
    """Install default model if not present"""
    print("📥 Checking for default model (mistral)...")
    
    success, output = run_command("ollama list", "Listing models")
    if "mistral" not in output:
        print("📥 Installing mistral model (this may take a few minutes)...")
        success, output = run_command("ollama pull mistral", "Downloading mistral model")
        if not success:
            print("❌ Failed to install mistral model")
            return False
        print("✅ Mistral model installed successfully")
    else:
        print("✅ Mistral model already available")
    
    return True


def test_installation():
    """Test the VEXA installation"""
    print("🧪 Testing VEXA installation...")
    
    try:
        # Try importing the agent
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from agent import create_vexa_agent, VexaConfig
        
        print("✅ VEXA modules imported successfully")
        
        # Try creating an agent (without actually running it)
        print("🤖 Testing agent creation...")
        agent = create_vexa_agent(model_name="mistral")
        health = agent.health_check()
        
        if health["status"] == "healthy":
            print("✅ Agent health check passed")
            return True
        else:
            print(f"⚠️ Agent health check warning: {health}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def main():
    """Main setup process"""
    print("🚀 VEXA AI Agent Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Check Ollama
    if not check_ollama():
        print("⚠️ Ollama issues detected. Please install and start Ollama before using VEXA.")
        print("📖 Visit: https://ollama.ai/ for installation instructions")
    else:
        # Install default model
        install_default_model()
    
    # Test installation
    if test_installation():
        print("\n🎉 VEXA setup completed successfully!")
        print("\n🚀 Next steps:")
        print("   1. Make sure Ollama is running: ollama serve")
        print("   2. Start CLI: python app/run_agent.py")
        print("   3. Start Web UI: python ui/web_ui.py")
        print("   4. Read README.md for more information")
    else:
        print("\n⚠️ Setup completed with warnings.")
        print("   Please check the issues above and ensure Ollama is properly configured.")


if __name__ == "__main__":
    main()
