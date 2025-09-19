import streamlit as st
from src.app.view.visual import VisualStructure
import os
from dotenv import load_dotenv

from src.agentic_ai.graph.graph_builder import GraphBuilder
from langchain_core.messages import AIMessage, SystemMessage


def main():
    _ = load_dotenv()
    config_path = os.environ["CONFIG_PATH"]

    if "messages" not in st.session_state:
        st.session_state["messages"] = list()

    if "model_state" not in st.session_state:
        st.session_state["model_state"] = list()
        msg = "Você é um agente de IA genérico que response no idioma da pergunta"
        st.session_state["model_state"].append(SystemMessage(content=msg))

    st.set_page_config(page_title="Agentic AI Model", layout="wide")

    visual = VisualStructure(config_path)

    visual.create_title()
    selected_model = visual.side_bar()

    visual.message_estructure(st.session_state, st.session_state["model_state"])

    graph_manager = GraphBuilder(selected_model)
    response = graph_manager.execute_graph(st.session_state["model_state"])

    if response:
        ai_response = response["messages"][-1].content
        st.session_state["model_state"].append(AIMessage(ai_response))

        visual.message_response(st.session_state, ai_response)


if __name__ == "__main__":
    main()
