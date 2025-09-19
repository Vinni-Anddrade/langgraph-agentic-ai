from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


class SearchTools:
    def __init__(self):
        self.instace_search_tools()

    def tavily_search_tool(self):
        """
        Makes a web search using Tavily operator. If you don't have one of the
        informations required, you are allowed to go to the web with this tool.
        """
        self.tavily_researcher = TavilySearchResults(maximum_results=3)

    def instace_search_tools(self):
        self.tavily_search_tool()

        self.search_tools = [
            self.tavily_researcher,
        ]
