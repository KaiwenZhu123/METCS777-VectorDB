"""
This module is responsibled for the Augementation - Generation Step in the RAG App,
and is implemented an Agent Tool. As user send a query thru the Chat, the following sequence
happens in this module:
- The query (string) is first encoded to Embeddings by `Cohere/Cohere-embed-english-v3.0`
- The query is passed to the Agent (backed by LLM) for it to determine intent
- Depending on the result of the first call returned by the LLM, the Agent then determine
if it wants to call `Retriever` from retrieve module
- Return the response to the caller

References:
https://python.langchain.com/docs/modules/agents/agent_types/openai_tools
"""
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Weaviate
from langchain.agents import AgentExecutor, create_openai_tools_agent
from prompt_template.agent_template import *
from prompt_template.retrieval_template import *


LLM = "gpt-3.5-turbo-1106"
TEMPERATURE = 0

class RAGController:
    def __init__(self):
        self.prompt = None
    
    def _init_tools(self):
        llm = ""
        tools = []
        prompt = []
        agent = create_openai_tools_agent(llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)

    def _create_prompt(self, query):
        self.prompt = PromptTemplate.from_template(
            AGENT_SYSTEM_PROMPT
        )
        return self.prompt

    def run(self, query):
        # prompt = self._create_prompt(query)  # call to init prompt
        agent_executor = self._init_tools()  # call to init_tools (tool need to be fresh each time)
        agent_executor.invoke({"input": query})