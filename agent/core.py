"""
Core agent logic for VEXA AI Agent using LangChain
"""
from langchain.agents import create_react_agent, AgentExecutor
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from typing import List, Dict, Any, Optional
import logging
import traceback

from .config import VexaConfig
from .tools import VexaTools


class VexaAgent:
    """Main VEXA AI Agent class"""
    
    def __init__(
        self, 
        model_name: str = None,
        tools: List[Tool] = None,
        verbose: bool = None
    ):
        """
        Initialize the VEXA Agent
        
        Args:
            model_name: Name of the Ollama model to use
            tools: List of tools for the agent
            verbose: Whether to show verbose output
        """
        self.model_name = model_name or VexaConfig.DEFAULT_MODEL
        self.verbose = verbose if verbose is not None else VexaConfig.VERBOSE
        self.tools = tools or VexaTools.get_default_tools()
        
        # Validate model
        if not VexaConfig.validate_model(self.model_name):
            logging.warning(f"Model {self.model_name} not in validated list. Proceeding anyway...")
        
        self.llm = None
        self.agent = None
        self.agent_executor = None
        
        self._initialize_agent()
    
    def _initialize_agent(self) -> None:
        """Initialize the LLM and agent"""
        try:
            # Initialize the LLM
            model_config = VexaConfig.get_model_config(self.model_name)
            self.llm = OllamaLLM(**model_config)
            
            # Create the prompt template
            prompt = self._create_prompt_template()
            
            # Create the agent
            self.agent = create_react_agent(self.llm, self.tools, prompt)
            
            # Create the agent executor
            agent_config = VexaConfig.get_agent_config()
            # Remove verbose from agent_config since it's passed separately
            agent_config_clean = {k: v for k, v in agent_config.items() if k != 'verbose'}
            
            self.agent_executor = AgentExecutor(
                agent=self.agent,
                tools=self.tools,
                verbose=self.verbose,
                **agent_config_clean
            )
            
        except Exception as e:
            logging.error(f"Failed to initialize agent: {e}")
            raise
    
    def _create_prompt_template(self) -> PromptTemplate:
        """Create a custom prompt template for the ReAct agent"""
        template = """You are VEXA, a helpful and intelligent AI assistant. You have access to various tools to help answer questions and perform tasks.

You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Important guidelines:
- Be helpful, accurate, and concise in your responses
- Use tools when you need current information or to perform specific tasks
- If you can answer directly without tools, feel free to do so
- Always provide the most accurate and up-to-date information possible
- If you're unsure about something, say so rather than guessing

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

        return PromptTemplate.from_template(template)
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        Process a query and return the response
        
        Args:
            question: The user's question or request
            
        Returns:
            Dictionary containing the response and metadata
        """
        if not self.agent_executor:
            raise RuntimeError("Agent not properly initialized")
        
        try:
            # Execute the query
            response = self.agent_executor.invoke({"input": question})
            
            return {
                "success": True,
                "response": response.get("output", "No response generated"),
                "input": question,
                "model": self.model_name,
                "tools_used": self._extract_tools_used(response)
            }
            
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            if self.verbose:
                error_msg += f"\nTraceback: {traceback.format_exc()}"
            
            logging.error(error_msg)
            return {
                "success": False,
                "response": "I encountered an error while processing your request. Please try rephrasing your question or check if Ollama is running with the correct model.",
                "error": str(e),
                "input": question,
                "model": self.model_name
            }
    
    def _extract_tools_used(self, response: Dict) -> List[str]:
        """Extract which tools were used in the response"""
        # This is a simplified implementation
        # In practice, you might want to parse the intermediate steps
        return []
    
    def add_tool(self, tool: Tool) -> None:
        """Add a new tool to the agent"""
        self.tools.append(tool)
        self._initialize_agent()  # Reinitialize with new tools
    
    def list_tools(self) -> str:
        """Get a list of available tools"""
        return VexaTools.list_available_tools()
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model"""
        return {
            "model_name": self.model_name,
            "available_models": VexaConfig.AVAILABLE_MODELS,
            "num_tools": len(self.tools),
            "tools": [tool.name for tool in self.tools]
        }
    
    def health_check(self) -> Dict[str, Any]:
        """Perform a health check on the agent"""
        try:
            # Try a simple query
            test_response = self.query("Say hello")
            return {
                "status": "healthy" if test_response["success"] else "unhealthy",
                "model": self.model_name,
                "tools_count": len(self.tools),
                "test_query_success": test_response["success"]
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "model": self.model_name,
                "tools_count": len(self.tools)
            }


def create_vexa_agent(
    model_name: str = None,
    custom_tools: List[Tool] = None,
    verbose: bool = None
) -> VexaAgent:
    """
    Factory function to create a VEXA agent
    
    Args:
        model_name: Ollama model name
        custom_tools: Custom tools to add
        verbose: Verbose output
        
    Returns:
        Configured VexaAgent instance
    """
    tools = VexaTools.get_default_tools()
    if custom_tools:
        tools.extend(custom_tools)
    
    return VexaAgent(
        model_name=model_name,
        tools=tools,
        verbose=verbose
    )
