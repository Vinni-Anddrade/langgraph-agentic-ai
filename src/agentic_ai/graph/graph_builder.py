from langgraph.graph import START, END, StateGraph

from src.agentic_ai.state.state_schema import StateSchema
from src.agentic_ai.nodes.nodes import SimpleChatbotNode


class GraphBuilder:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.graph = StateGraph(state_schema=StateSchema)

    def simple_chatbot_graph(self):

        nodes_manager = SimpleChatbotNode(self.model_name)

        self.graph.add_node("llm_brain", nodes_manager.llm_brain)

        self.graph.add_edge(START, "llm_brain")
        self.graph.add_edge("llm_brain", END)
        self.graph_model = self.graph.compile()

    def execute_graph(self, model_state, use_case: str):
        if len(model_state) > 0:
            if use_case == "Basic Chatbot":
                self.simple_chatbot_graph()
                return self.graph_model.invoke(input={"messages": model_state})
