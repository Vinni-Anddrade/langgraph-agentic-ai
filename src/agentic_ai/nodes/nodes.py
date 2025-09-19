from src.agentic_ai.llm.llm_model import GroqModel
from src.agentic_ai.state.state_schema import StateSchema


class SimpleChatbotNode:
    def __init__(self, model_name: str, tools):
        self.tools = tools
        self.model_name = model_name
        self.llm_model = GroqModel(self.model_name)
        self.llm_model = self.llm_model.llm_model.bind_tools(tools=self.tools)

    def llm_brain(self, state: StateSchema) -> dict:
        """
        Chatbot Brain node. Only return a response without source knowledge.
        It only responds with its own training knowledge.
        """

        return {"messages": self.llm_model.invoke(state["messages"])}
