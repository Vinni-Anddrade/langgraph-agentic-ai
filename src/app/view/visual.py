import streamlit as st
from src.app.utils.utils import read_yaml
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


class VisualStructure:
    def __init__(self, config_path: str):
        self.config = read_yaml(config_path)

    def create_title(self):
        st.title("Agentic AI Chatbot")

    def side_bar(self):

        st.sidebar.title("Agent Configuration")
        model = st.sidebar.selectbox(
            label="Model Selection: ", options=self.config["models"]
        )
        usage_type = st.sidebar.selectbox(
            label="Select Usage: ", options=self.config["use_case_models"]
        )

        return model, usage_type

    def message_estructure(self, session_state, model_state: list):
        for msg in session_state["messages"]:
            if msg["role"] == "user":
                st.chat_message("user").markdown(msg["content"])
            else:
                st.chat_message("assistant").markdown(msg["content"])

        if prompt := st.chat_input("Escreva uma mensagem"):
            model_state.append(HumanMessage(prompt))
            session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user").markdown(prompt)

        return model_state

    def message_response(self, session_state, model_response):
        if len(session_state["messages"]) > 0:
            last_chat = session_state["messages"][-1]
            if last_chat["role"] == "user":
                session_state["messages"].append(
                    {"role": "assistant", "content": model_response}
                )
                st.chat_message("assistant").markdown(model_response)
