"""
Custom tools for the VEXA AI Agent
"""
from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List
import datetime
import math
import json
import requests


class VexaTools:
    """Collection of tools for the VEXA AI Agent"""
    
    @staticmethod
    def get_web_search_tool() -> Tool:
        """Web search tool using DuckDuckGo"""
        search = DuckDuckGoSearchRun()
        return Tool(
            name="web_search",
            func=search.run,
            description="Useful for searching the web for current information, news, facts, and answers. Input should be a search query string."
        )
    
    @staticmethod
    def get_calculator_tool() -> Tool:
        """Calculator tool for mathematical operations"""
        def calculate(expression: str) -> str:
            """Safely evaluate mathematical expressions"""
            try:
                # Remove any potentially dangerous operations
                allowed_chars = set('0123456789+-*/().** ')
                if not all(c in allowed_chars for c in expression.replace(' ', '')):
                    return "Error: Invalid characters in expression. Only numbers and basic math operators (+, -, *, /, **, ()) are allowed."
                
                # Evaluate the expression safely
                result = eval(expression, {"__builtins__": {}}, {"math": math})
                return f"Result: {result}"
            except Exception as e:
                return f"Error calculating '{expression}': {str(e)}"
        
        return Tool(
            name="calculator",
            func=calculate,
            description="Useful for performing mathematical calculations. Input should be a mathematical expression like '2+2' or 'sqrt(16)'. Supports basic operations: +, -, *, /, **, ()."
        )
    
    @staticmethod
    def get_datetime_tool() -> Tool:
        """Tool for getting current date and time information"""
        def get_datetime_info(query: str = "") -> str:
            """Get current date/time information"""
            now = datetime.datetime.now()
            
            if "date" in query.lower():
                return f"Current date: {now.strftime('%Y-%m-%d')}"
            elif "time" in query.lower():
                return f"Current time: {now.strftime('%H:%M:%S')}"
            else:
                return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        
        return Tool(
            name="datetime",
            func=get_datetime_info,
            description="Get current date and time information. Use 'date' for just date, 'time' for just time, or leave empty for both."
        )
    
    @staticmethod
    def get_weather_tool() -> Tool:
        """Simple weather tool (placeholder for demonstration)"""
        def get_weather(location: str) -> str:
            """Get weather information for a location"""
            try:
                # This is a placeholder - in production, you'd use a real weather API
                return f"Weather tool is available but requires API configuration for location: {location}. Use web search for current weather information instead."
            except Exception as e:
                return f"Error getting weather for {location}: {str(e)}"
        
        return Tool(
            name="weather",
            func=get_weather,
            description="Get weather information for a specific location. Input should be a city name or location."
        )
    
    @staticmethod
    def get_file_operations_tool() -> Tool:
        """File operations tool for basic file tasks"""
        def file_operations(operation: str) -> str:
            """Perform basic file operations"""
            try:
                if operation.startswith("list"):
                    import os
                    path = operation.replace("list ", "").strip() or "."
                    files = os.listdir(path)
                    return f"Files in '{path}': {', '.join(files[:10])}{'...' if len(files) > 10 else ''}"
                elif operation.startswith("pwd"):
                    import os
                    return f"Current directory: {os.getcwd()}"
                else:
                    return "Supported operations: 'list [path]' to list files, 'pwd' for current directory"
            except Exception as e:
                return f"Error with file operation '{operation}': {str(e)}"
        
        return Tool(
            name="file_ops",
            func=file_operations,
            description="Basic file operations. Use 'list' to list files in current directory, 'list [path]' for specific directory, or 'pwd' for current working directory."
        )
    
    @classmethod
    def get_default_tools(cls) -> List[Tool]:
        """Get the default set of tools for the agent"""
        return [
            cls.get_web_search_tool(),
            cls.get_calculator_tool(),
            cls.get_datetime_tool(),
            cls.get_file_operations_tool(),
        ]
    
    @classmethod
    def get_all_tools(cls) -> List[Tool]:
        """Get all available tools"""
        return [
            cls.get_web_search_tool(),
            cls.get_calculator_tool(),
            cls.get_datetime_tool(),
            cls.get_weather_tool(),
            cls.get_file_operations_tool(),
        ]
    
    @classmethod
    def list_available_tools(cls) -> str:
        """Get a formatted list of available tools"""
        tools_info = [
            "🔍 web_search - Search the web for information",
            "🧮 calculator - Perform mathematical calculations", 
            "📅 datetime - Get current date and time",
            "📁 file_ops - Basic file operations",
            "🌤️ weather - Weather information (placeholder)"
        ]
        return "Available tools:\n" + "\n".join(tools_info)
