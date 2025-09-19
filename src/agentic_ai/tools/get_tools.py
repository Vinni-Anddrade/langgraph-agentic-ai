from src.agentic_ai.tools.search_tool import SearchTools


class GetTools:
    def __init__(self):
        self.tools = list()

        self.get_tools()

    def get_tools(self):
        self.tools += SearchTools().search_tools
