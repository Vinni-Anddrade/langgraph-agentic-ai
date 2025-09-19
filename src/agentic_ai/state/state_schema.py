from typing import TypedDict, Annotated, List
from langgraph.graph.message import add_messages


class StateSchema(TypedDict):
    """
    It is the State Structure of the graph
    """

    messages: Annotated[List, add_messages]
