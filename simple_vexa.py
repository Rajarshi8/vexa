#!/usr/bin/env python3
"""
VEXA Interactive Mode - Works without Ollama

This provides a simple interactive interface using VEXA tools
without requiring Ollama to be running.
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

from agent import VexaTools, VexaConfig

class SimpleVEXA:
    """Simple VEXA interface without LLM"""
    
    def __init__(self):
        self.tools = {
            'calculator': VexaTools.get_calculator_tool(),
            'datetime': VexaTools.get_datetime_tool(), 
            'file_ops': VexaTools.get_file_operations_tool()
        }
        print("🤖 Simple VEXA initialized!")
        print("Available tools:", list(self.tools.keys()))
    
    def process_query(self, query: str) -> str:
        """Process user query with available tools"""
        query_lower = query.lower()
        
        # Calculator queries
        if any(word in query_lower for word in ['calculate', 'math', '+', '-', '*', '/', '=']):
            if any(op in query for op in ['+', '-', '*', '/']):
                # Extract the math expression
                import re
                match = re.search(r'([0-9+\-*/\.\(\)\s]+)', query)
                if match:
                    expression = match.group(1).strip()
                    return self.tools['calculator'].func(expression)
            return self.tools['calculator'].func(query)
        
        # DateTime queries
        elif any(word in query_lower for word in ['time', 'date', 'today', 'now']):
            return self.tools['datetime'].func(query)
        
        # File operations
        elif any(word in query_lower for word in ['list', 'files', 'directory', 'folder']):
            return self.tools['file_ops'].func(query)
        
        # Help
        elif any(word in query_lower for word in ['help', 'tools', 'commands']):
            return """Available commands:
🧮 Calculator: "calculate 2+2", "what's 15*23?"
📅 DateTime: "what time is it?", "current date"
📁 Files: "list files", "show directory"
❓ Help: "help", "tools"
🚪 Exit: "exit", "quit", "bye"""
        
        # General response
        else:
            return f"I received: '{query}'\n\nI'm in simple mode without LLM. Try:\n• Math: '2+2' or 'calculate 15*23'\n• Time: 'what time is it?'\n• Files: 'list files'\n• Help: 'help'"

def main():
    print(VexaConfig.get_welcome_message())
    print("\n🔧 Running in Simple Mode (No Ollama required)")
    print("="*50)
    
    vexa = SimpleVEXA()
    
    while True:
        try:
            query = input("\n🤔 Ask me anything (or 'exit'): ").strip()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
            
        if not query:
            continue
            
        if query.lower() in ['exit', 'quit', 'bye', 'q']:
            print("👋 Goodbye!")
            break
            
        print("-" * 40)
        response = vexa.process_query(query)
        print(f"🤖 VEXA: {response}")

if __name__ == "__main__":
    main()
