#!/usr/bin/env python3
"""
Web UI for VEXA AI Agent using Gradio

A simple web interface for interacting with the VEXA AI Agent.
Provides a clean, ChatGPT-like experience in the browser.
"""

import gradio as gr
import sys
import os
import logging
from typing import List, Tuple, Optional
import traceback

# Add parent directory to path to import agent module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import VexaAgent, create_vexa_agent, VexaConfig


class VexaWebUI:
    """Web UI class for VEXA Agent"""
    
    def __init__(self, model_name: str = None, port: int = None):
        """Initialize the web UI"""
        self.model_name = model_name or VexaConfig.DEFAULT_MODEL
        self.port = port or VexaConfig.WEB_UI_PORT
        self.agent: Optional[VexaAgent] = None
        self.chat_history: List[Tuple[str, str]] = []
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        
    def initialize_agent(self) -> Tuple[bool, str]:
        """Initialize the agent"""
        try:
            self.agent = create_vexa_agent(
                model_name=self.model_name,
                verbose=False  # Disable verbose for web UI
            )
            
            # Perform health check
            health = self.agent.health_check()
            if health["status"] == "healthy":
                return True, f"✅ Agent initialized with model: {self.model_name}"
            else:
                return False, f"❌ Health check failed: {health.get('error', 'Unknown error')}"
                
        except Exception as e:
            return False, f"❌ Failed to initialize: {str(e)}"
    
    def chat_response(self, message: str, history: List[List[str]]) -> Tuple[str, List[List[str]]]:
        """Process chat message and return response"""
        if not self.agent:
            success, msg = self.initialize_agent()
            if not success:
                return "", history + [[message, f"🚨 {msg}\n\nPlease ensure Ollama is running with the {self.model_name} model."]]
        
        try:
            # Process the query
            response = self.agent.query(message)
            
            if response["success"]:
                bot_response = f"🤖 {response['response']}"
            else:
                bot_response = f"❌ {response['response']}"
            
            # Update history
            history.append([message, bot_response])
            return "", history
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            history.append([message, error_msg])
            return "", history
    
    def get_model_info(self) -> str:
        """Get model information"""
        if not self.agent:
            return "Agent not initialized"
        
        info = self.agent.get_model_info()
        return f"""
**Current Model:** {info['model_name']}  
**Available Models:** {', '.join(info['available_models'])}  
**Tools Available:** {info['num_tools']}  
**Tool Names:** {', '.join(info['tools'])}
        """.strip()
    
    def get_tools_info(self) -> str:
        """Get tools information"""
        if self.agent:
            return self.agent.list_tools()
        else:
            from agent.tools import VexaTools
            return VexaTools.list_available_tools()
    
    def clear_chat(self) -> List:
        """Clear chat history"""
        return []
    
    def create_interface(self) -> gr.Blocks:
        """Create the Gradio interface"""
        
        # Custom CSS for better styling
        custom_css = """
        .gradio-container {
            max-width: 1200px !important;
            margin: auto;
        }
        .header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #666;
        }
        """
        
        with gr.Blocks(
            title="VEXA AI Agent",
            theme=gr.themes.Soft(),
            css=custom_css
        ) as interface:
            
            # Header
            gr.HTML("""
            <div class="header">
                <h1>🤖 VEXA AI Agent</h1>
                <p>Privacy-focused • Offline-capable • Powered by Open-Source LLMs</p>
            </div>
            """)
            
            # Main chat interface
            with gr.Row():
                with gr.Column(scale=4):
                    chatbot = gr.Chatbot(
                        label="Chat with VEXA",
                        height=500,
                        show_label=True,
                        container=True,
                        bubble_full_width=False
                    )
                    
                    with gr.Row():
                        msg = gr.Textbox(
                            placeholder="Ask me anything...",
                            container=False,
                            scale=4,
                            lines=1
                        )
                        submit_btn = gr.Button("Send", scale=1, variant="primary")
                        clear_btn = gr.Button("Clear", scale=1, variant="secondary")
                
                # Sidebar with info
                with gr.Column(scale=1):
                    gr.Markdown("## 📊 Model Info")
                    model_info = gr.Markdown(self.get_model_info())
                    refresh_info_btn = gr.Button("🔄 Refresh Info", size="sm")
                    
                    gr.Markdown("## 🛠️ Available Tools")
                    tools_info = gr.Markdown(self.get_tools_info())
                    
                    gr.Markdown("## 💡 Example Queries")
                    examples = gr.Markdown("""
                    • What's the current date?
                    • Calculate 25 * 17 + 100
                    • Search for latest AI news
                    • List files in directory
                    • What's 2+2?
                    """)
            
            # Event handlers
            def respond(message, chat_history):
                return self.chat_response(message, chat_history)
            
            # Submit on Enter or button click
            msg.submit(respond, [msg, chatbot], [msg, chatbot])
            submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
            
            # Clear chat
            clear_btn.click(self.clear_chat, [], [chatbot])
            
            # Refresh model info
            refresh_info_btn.click(lambda: self.get_model_info(), [], [model_info])
            
            # Footer
            gr.HTML("""
            <div class="footer">
                <p>VEXA v1.0.0 | Built with ❤️ using LangChain, Ollama & Gradio</p>
                <p>🔒 Your conversations are private and processed locally</p>
            </div>
            """)
        
        return interface
    
    def launch(self, share: bool = False, debug: bool = False):
        """Launch the web interface"""
        print(f"🚀 Starting VEXA Web UI...")
        print(f"   Model: {self.model_name}")
        print(f"   Port: {self.port}")
        print(f"   Share: {share}")
        
        interface = self.create_interface()
        
        try:
            interface.launch(
                server_port=self.port,
                share=share,
                debug=debug,
                show_error=True,
                server_name="0.0.0.0" if share else "127.0.0.1"
            )
        except Exception as e:
            print(f"❌ Failed to launch web UI: {e}")
            if debug:
                traceback.print_exc()


def main():
    """Main entry point for web UI"""
    import argparse
    
    parser = argparse.ArgumentParser(description="VEXA AI Agent Web UI")
    parser.add_argument(
        "--model", "-m",
        default=VexaConfig.DEFAULT_MODEL,
        help=f"Ollama model to use (default: {VexaConfig.DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=VexaConfig.WEB_UI_PORT,
        help=f"Port to run web UI (default: {VexaConfig.WEB_UI_PORT})"
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Create public share link"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Create and launch web UI
    web_ui = VexaWebUI(model_name=args.model, port=args.port)
    web_ui.launch(share=args.share, debug=args.debug)


if __name__ == "__main__":
    main()
