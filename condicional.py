from langgraph.graph import StateGraph, START, END
from IPython.display import display,Image
from typing import Literal,TypedDict
import random

class State(TypedDict):
    graph_state : str

def node_1(state):
    print(" I m in node 1")
    return {"graph_state" : state["graph_state"] + " I am "}

def node_2(state):
    print(" I m in node 2")
    return {"graph_state" : state["graph_state"] + " Happy "}

def node_3(state):
    print(" I m in node 3")
    return {"graph_state" : state["graph_state"] + " Sad "}

def condition_node(state) -> Literal["node_2", "node_3"]:
    if random.random() < 0.5:
        return "node_2"
    return "node_3"


builder = StateGraph(State)

builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", condition_node)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

graph = builder.compile()

Image(graph.get_graph().draw_mermaid_png())