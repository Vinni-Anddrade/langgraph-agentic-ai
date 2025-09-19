from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from src.agentic_ai.state.state_schema import StateSchema
from src.agentic_ai.nodes.nodes import SimpleChatbotNode
from src.agentic_ai.tools.get_tools import GetTools


class GraphBuilder:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.graph = StateGraph(state_schema=StateSchema)
        self.tools = GetTools().tools

        self.chatbot_graph()
        self.graph_model = self.graph.compile()

    def chatbot_graph(self):
        nodes_manager = SimpleChatbotNode(self.model_name, self.tools)

        self.graph.add_node("llm_brain", nodes_manager.llm_brain)
        self.graph.add_node("tools", ToolNode(self.tools))

        self.graph.add_edge(START, "llm_brain")
        self.graph.add_conditional_edges("llm_brain", tools_condition)
        self.graph.add_edge("tools", "llm_brain")

    def execute_graph(self, model_state):
        if len(model_state) > 0:
            return self.graph_model.invoke(input={"messages": model_state})
