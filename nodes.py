from app.intents import detect_intent
from app.rag import load_retriever, simple_search

def intent_node(state):
    text = state["messages"][-1]
    intent = detect_intent(text)
    state["intent"] = intent
    return state

def rag_node(state):
    docs = load_retriever()
    query = state["messages"][-1]
    answer = simple_search(query, docs)
    state["messages"].append(answer)
    return state

def lead_node(state):
    state["messages"].append("Lead captured successfully.")
    return state

def tool_node(state):
    state["messages"].append("Tool executed locally.")
    return state
