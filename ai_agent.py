"""
LEGACY VERSION - Simple VEXA AI Agent

This is the original simple version of VEXA. 
For the full-featured version, use the new modular structure:
- CLI: python app/run_agent.py
- Web UI: python ui/web_ui.py
- Setup: python setup.py
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
import datetime

# Load a local LLM like Mistral or Llama2 (must have Ollama running)
llm = OllamaLLM(model="mistral")

# Setup web search tool
search = DuckDuckGoSearchRun()

# Define tools the agent can use
tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for searching the web"
    )
]

# Create a prompt template for the ReAct agent
prompt = PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

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

Begin!

Question: {input}
Thought:{agent_scratchpad}""")

# Create the agent
agent = create_react_agent(llm, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Get user input and run
while True:
    query = input("\nAsk me anything (or type 'exit'): ")
    if query.lower() == 'exit':
        break
    response = agent_executor.invoke({"input": query})
    print(f"\n🤖: {response['output']}")

print("\n👋 Thanks for using VEXA!")
print("💡 Try the full version with: python app/run_agent.py")
