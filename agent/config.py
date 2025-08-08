"""
Configuration settings for the VEXA AI Agent
"""
import os
from typing import Dict, List

class VexaConfig:
    """Configuration class for VEXA AI Agent"""
    
    # Default LLM settings
    DEFAULT_MODEL = "mistral"
    AVAILABLE_MODELS = [
        "mistral",
        "llama2",
        "llama3",
        "codellama",
        "neural-chat",
        "orca-mini"
    ]
    
    # Agent settings
    AGENT_NAME = "VEXA"
    AGENT_VERSION = "1.0.0"
    MAX_ITERATIONS = 10
    VERBOSE = True
    
    # Search settings
    SEARCH_RESULTS_LIMIT = 5
    SEARCH_TIMEOUT = 30
    
    # UI settings
    WEB_UI_PORT = 7860
    WEB_UI_SHARE = False
    
    @classmethod
    def get_model_config(cls, model_name: str = None) -> Dict:
        """Get model configuration"""
        model = model_name or cls.DEFAULT_MODEL
        return {
            "model": model,
            "temperature": 0.7,
            "top_p": 0.9,
            "num_predict": 2048,
        }
    
    @classmethod
    def get_agent_config(cls) -> Dict:
        """Get agent configuration"""
        return {
            "max_iterations": cls.MAX_ITERATIONS,
            "early_stopping_method": "generate",
            "handle_parsing_errors": True,
        }
    
    @classmethod
    def validate_model(cls, model_name: str) -> bool:
        """Validate if model is supported"""
        return model_name in cls.AVAILABLE_MODELS
    
    @classmethod
    def get_welcome_message(cls) -> str:
        """Get welcome message"""
        return f"""
🤖 Welcome to {cls.AGENT_NAME} v{cls.AGENT_VERSION}!
   
✅ Privacy-focused AI Assistant
🔍 Web search capabilities  
🖥️  100% offline-ready
🔧 Powered by open-source LLMs

Type your question or 'exit' to quit.
        """.strip()
