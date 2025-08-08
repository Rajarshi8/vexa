#!/usr/bin/env python3
"""
VEXA Demo Mode - Works without Ollama for demonstration

This demo mode shows VEXA functionality without requiring Ollama to be installed.
It uses simulated responses to demonstrate the agent's capabilities.
"""

import sys
import os

import sys
import os
import datetime
import math
import json

# Add current directory and agent directory to path for imports
current_dir = os.getcwd()
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'agent'))

try:
    from agent import VexaConfig
except ImportError:
    # Fallback if agent module not available
    class VexaConfig:
        AVAILABLE_MODELS = ["mistral", "llama2", "llama3"]


class VexaDemo:
    """Demo version of VEXA that works without Ollama"""
    
    def __init__(self):
        self.model_name = "demo-mode"
        self.tools = [
            "web_search", "calculator", "datetime", "file_ops", "weather"
        ]
    
    def query(self, question: str) -> dict:
        """Process query in demo mode"""
        question_lower = question.lower()
        
        # Calculator responses
        if any(op in question for op in ['+', '-', '*', '/', 'calculate', 'math']):
            return self._handle_math(question)
        
        # Time/date responses
        elif any(word in question_lower for word in ['time', 'date', 'today']):
            return self._handle_datetime(question)
        
        # Search responses
        elif any(word in question_lower for word in ['search', 'news', 'weather', 'find']):
            return self._handle_search(question)
        
        # File operations
        elif any(word in question_lower for word in ['list', 'files', 'directory']):
            return self._handle_files(question)
        
        # General responses
        else:
            return self._handle_general(question)
    
    def _handle_math(self, question: str) -> dict:
        """Handle mathematical queries"""
        try:
            # Try to extract and calculate simple expressions
            import re
            # Look for simple math expressions
            match = re.search(r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)', question)
            if match:
                num1, op, num2 = float(match.group(1)), match.group(2), float(match.group(3))
                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
                
                return {
                    "success": True,
                    "response": f"I'll calculate that for you.\n\nUsing the calculator tool:\nResult: {result}"
                }
        except:
            pass
        
        return {
            "success": True,
            "response": "I can help with calculations! In the full version with Ollama, I would use the calculator tool to solve mathematical expressions like this one."
        }
    
    def _handle_datetime(self, question: str) -> dict:
        """Handle date/time queries"""
        now = datetime.datetime.now()
        return {
            "success": True,
            "response": f"Using the datetime tool:\nCurrent date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        }
    
    def _handle_search(self, question: str) -> dict:
        """Handle search queries"""
        return {
            "success": True,
            "response": f"I would search for information about: '{question}'\n\nIn the full version, I use DuckDuckGo to find real-time information from the web. This requires an internet connection and the full VEXA setup with Ollama."
        }
    
    def _handle_files(self, question: str) -> dict:
        """Handle file operation queries"""
        try:
            files = os.listdir('.')[:10]  # Limit to 10 files
            file_list = ', '.join(files)
            return {
                "success": True,
                "response": f"Using the file_ops tool:\nFiles in current directory: {file_list}"
            }
        except:
            return {
                "success": True,
                "response": "I can list files and perform basic file operations in the full version."
            }
    
    def _handle_general(self, question: str) -> dict:
        """Handle general queries"""
        responses = [
            f"Hello! I'm VEXA running in demo mode. Your question was: '{question}'",
            "In the full version with Ollama, I can provide detailed answers, search the web, and use various tools to help you.",
            "This demo shows the structure and capabilities of VEXA without requiring Ollama to be installed."
        ]
        
        return {
            "success": True,
            "response": "\n\n".join(responses)
        }
    
    def get_model_info(self) -> dict:
        """Get model information"""
        return {
            "model_name": self.model_name,
            "available_models": ["demo-mode"] + VexaConfig.AVAILABLE_MODELS,
            "num_tools": len(self.tools),
            "tools": self.tools
        }


def main():
    """Demo CLI interface"""
    print("🎮 VEXA Demo Mode")
    print("=" * 50)
    print("This demo shows VEXA functionality without requiring Ollama.")
    print("For the full experience, install Ollama and use the regular version.")
    print("=" * 50)
    
    demo = VexaDemo()
    
    # Demo queries
    demo_queries = [
        "What's 15 + 27?",
        "What time is it?",
        "Search for AI news",
        "List files in directory",
        "Hello VEXA!"
    ]
    
    print("\n🎯 Running demo queries:\n")
    
    for query in demo_queries:
        print(f"🤔 Query: {query}")
        print("-" * 40)
        response = demo.query(query)
        print(f"🤖 VEXA: {response['response']}")
        print("\n" + "="*50 + "\n")
    
    print("🎉 Demo completed!")
    print("\n📖 To run the full version:")
    print("   1. Install Ollama: https://ollama.ai/")
    print("   2. Start Ollama: ollama serve")
    print("   3. Pull a model: ollama pull mistral")
    print("   4. Run: python app/run_agent.py")


if __name__ == "__main__":
    main()
