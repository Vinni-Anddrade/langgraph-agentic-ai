from dotenv import load_dotenv
from langchain_groq import ChatGroq


_ = load_dotenv()


class GroqModel:
    def __init__(self, selected_model: str):
        self.selected_model = selected_model
        self.model_instance()

    def model_instance(self):
        try:
            self.llm_model = ChatGroq(model=self.selected_model, temperature=0.0)
        except Exception as e:
            ValueError(f"No model could be loaded. There was an error: \n\n {e}")
