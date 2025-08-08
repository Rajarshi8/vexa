#!/usr/bin/env python3
"""
CLI Runner for VEXA AI Agent

Usage:
    python run_agent.py [options]
    
Examples:
    python run_agent.py                    # Use default model
    python run_agent.py --model llama2     # Use specific model
    python run_agent.py --verbose          # Enable verbose mode
    python run_agent.py --tools-info       # Show available tools
"""

import argparse
import sys
import os
import logging
from typing import Optional

# Add parent directory to path to import agent module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import VexaAgent, create_vexa_agent, VexaConfig


class VexaCLI:
    """Command-line interface for VEXA Agent"""
    
    def __init__(self, model_name: str = None, verbose: bool = False):
        """Initialize CLI with agent"""
        self.model_name = model_name or VexaConfig.DEFAULT_MODEL
        self.verbose = verbose
        self.agent: Optional[VexaAgent] = None
        
        # Setup logging
        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def initialize_agent(self) -> bool:
        """Initialize the agent"""
        try:
            print(f"🔄 Initializing VEXA with model: {self.model_name}")
            print("   (Make sure Ollama is running with the specified model)")
            
            self.agent = create_vexa_agent(
                model_name=self.model_name,
                verbose=self.verbose
            )
            
            # Perform health check
            health = self.agent.health_check()
            if health["status"] == "healthy":
                print("✅ Agent initialized successfully!")
                return True
            else:
                print(f"❌ Agent health check failed: {health.get('error', 'Unknown error')}")
                return False
                
        except Exception as e:
            print(f"❌ Failed to initialize agent: {e}")
            print("\n💡 Troubleshooting tips:")
            print("   1. Make sure Ollama is running: ollama serve")
            print(f"   2. Make sure the model is installed: ollama pull {self.model_name}")
            print("   3. Check if the model name is correct")
            return False
    
    def show_welcome(self):
        """Show welcome message"""
        print(VexaConfig.get_welcome_message())
        if self.agent:
            print(f"\n🔧 Model: {self.model_name}")
            print(f"🛠️  Tools: {len(self.agent.tools)} available")
        print("\n" + "="*50)
    
    def show_tools_info(self):
        """Show information about available tools"""
        print("\n" + "="*50)
        print("🛠️  VEXA TOOLS INFORMATION")
        print("="*50)
        
        if self.agent:
            print(self.agent.list_tools())
        else:
            from agent.tools import VexaTools
            print(VexaTools.list_available_tools())
        
        print("\nExample queries:")
        print("  • What's the weather like in New York?")
        print("  • Calculate 15 * 23 + 45")
        print("  • What's the current date?")
        print("  • Search for latest AI news")
        print("  • List files in current directory")
    
    def run_interactive(self):
        """Run interactive chat mode"""
        if not self.agent:
            if not self.initialize_agent():
                return
        
        self.show_welcome()
        
        try:
            while True:
                # Get user input
                try:
                    query = input("\n🤔 Ask me anything (or 'exit'): ").strip()
                except KeyboardInterrupt:
                    print("\n👋 Goodbye!")
                    break
                
                if not query:
                    continue
                    
                # Check for exit commands
                if query.lower() in ['exit', 'quit', 'bye', 'q']:
                    print("👋 Goodbye!")
                    break
                
                # Check for special commands
                if query.lower() in ['help', 'tools', 'tools-info']:
                    self.show_tools_info()
                    continue
                
                if query.lower() in ['model', 'info']:
                    info = self.agent.get_model_info()
                    print(f"\n📊 Model: {info['model_name']}")
                    print(f"🛠️  Tools: {', '.join(info['tools'])}")
                    continue
                
                # Process the query
                print(f"\n🤖 Processing: {query}")
                print("-" * 40)
                
                response = self.agent.query(query)
                
                if response["success"]:
                    print(f"\n✅ VEXA: {response['response']}")
                else:
                    print(f"\n❌ Error: {response['response']}")
                    if self.verbose and 'error' in response:
                        print(f"Details: {response['error']}")
                
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
    
    def run_single_query(self, query: str):
        """Run a single query and exit"""
        if not self.agent:
            if not self.initialize_agent():
                return
        
        print(f"🤖 Query: {query}")
        print("-" * 50)
        
        response = self.agent.query(query)
        
        if response["success"]:
            print(f"✅ Response: {response['response']}")
        else:
            print(f"❌ Error: {response['response']}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="VEXA - Privacy-focused AI Agent",
        epilog="""
Examples:
  python run_agent.py                    # Interactive mode with default model
  python run_agent.py --model llama2     # Use specific model
  python run_agent.py --query "Hello"    # Single query mode
  python run_agent.py --tools-info       # Show available tools
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--model", "-m",
        default=VexaConfig.DEFAULT_MODEL,
        help=f"Ollama model to use (default: {VexaConfig.DEFAULT_MODEL})"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    parser.add_argument(
        "--query", "-q",
        help="Run a single query and exit"
    )
    
    parser.add_argument(
        "--tools-info",
        action="store_true",
        help="Show available tools information and exit"
    )
    
    parser.add_argument(
        "--models",
        action="store_true",
        help="List available models and exit"
    )
    
    args = parser.parse_args()
    
    # Handle special commands
    if args.models:
        print("📋 Available models:")
        for model in VexaConfig.AVAILABLE_MODELS:
            marker = " (default)" if model == VexaConfig.DEFAULT_MODEL else ""
            print(f"   • {model}{marker}")
        return
    
    # Create CLI instance
    cli = VexaCLI(model_name=args.model, verbose=args.verbose)
    
    if args.tools_info:
        cli.show_tools_info()
        return
    
    if args.query:
        cli.run_single_query(args.query)
        return
    
    # Run interactive mode
    cli.run_interactive()


if __name__ == "__main__":
    main()
