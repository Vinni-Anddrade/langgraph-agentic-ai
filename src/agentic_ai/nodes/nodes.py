from src.agentic_ai.llm.llm_model import GroqModel
from src.agentic_ai.state.state_schema import StateSchema


class SimpleChatbotNode:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def llm_brain(self, state: StateSchema) -> dict:
        """
        Chatbot Brain node. Only return a response without source knowledge.
        It only responds with its own training knowledge.
        """

        model_manager = GroqModel(self.model_name)
        self.llm_model = model_manager.llm_model

        return {"messages": self.llm_model.invoke(state["messages"])}
