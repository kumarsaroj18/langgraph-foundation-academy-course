import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Conditional edge
def decide_mood(state) -> Literal["happy", "sad"]:
    
    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 
    
    # Here, let's just do a 50 / 50 split between nodes 2, 3
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "happy"
    
    # 50% of the time, we return Node 3
    return "sad"

# Nodes
def mood(state):
    print("---Node 1---")
    return {"graph_state":state['graph_state'] +" I am"}

def happy(state):
    print("---Node 2---")
    return {"graph_state":state['graph_state'] +" happy!"}

def sad(state):
    print("---Node 3---")
    return {"graph_state":state['graph_state'] +" sad!"}

# Build graph
builder = StateGraph(State)
builder.add_node("mood", mood)
builder.add_node("happy", happy)
builder.add_node("sad", sad)
builder.add_edge(START, "mood")
builder.add_conditional_edges("mood", decide_mood)
builder.add_edge("happy", END)
builder.add_edge("sad", END)

# Compile graph
graph = builder.compile()