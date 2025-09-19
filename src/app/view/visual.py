import streamlit as st
from src.app.utils.utils import read_yaml
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


class VisualStructure:
    def __init__(self, config_path: str):
        self.config = read_yaml(config_path)
        self.user_avatar = (
            "https://icons.veryicon.com/png/o/internet--web/prejudice/user-128.png"
        )
        self.chat_avatar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9csgY-MMUWpBriZsN30BCmtjz3tjOXQRptA&s"

    def create_title(self):
        st.title("Agentic AI Chatbot")

    def side_bar(self):

        st.sidebar.title("Agent Configuration")
        model = st.sidebar.selectbox(
            label="Model Selection: ", options=self.config["models"]
        )

        return model

    def message_estructure(self, session_state, model_state: list):
        for msg in session_state["messages"]:
            if msg["role"] == "user":
                st.chat_message("user", avatar=self.user_avatar).markdown(
                    msg["content"]
                )
            else:
                st.chat_message("assistant", avatar=self.chat_avatar).markdown(
                    msg["content"]
                )

        if prompt := st.chat_input("Escreva uma mensagem"):
            model_state.append(HumanMessage(prompt))
            session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user", avatar=self.user_avatar).markdown(prompt)

        return model_state

    def message_response(self, session_state, model_response):
        if len(session_state["messages"]) > 0:
            last_chat = session_state["messages"][-1]
            if last_chat["role"] == "user":
                session_state["messages"].append(
                    {"role": "assistant", "content": model_response}
                )
                st.chat_message("assistant", avatar=self.chat_avatar).markdown(
                    model_response
                )
