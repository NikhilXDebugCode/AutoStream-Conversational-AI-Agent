from langgraph.graph import StateGraph, END
from app.intents import detect_intent
from app.rag import rag_answer
from app.tools import mock_lead_capture


def agent_node(state: dict) -> dict:
    user_input = state.get("user_input", "").strip()
    state.setdefault("messages", [])

    intent = detect_intent(user_input)
    state["intent"] = intent

    # 1. Greeting
    if intent == "greeting":
        response = "Hello! How can I help you today?"
        print(response)
        state["messages"].append(response)
        return state

    # 2. Pricing / RAG
    if intent == "pricing":
        response = rag_answer(user_input)
        print(response)
        state["messages"].append(response)
        return state

    # 3. High-intent lead flow
    if intent == "high_intent":
        if "name" not in state:
            state["name"] = input("What is your name? ")

        if "email" not in state:
            state["email"] = input("What is your email? ")

        if "platform" not in state:
            state["platform"] = input(
                "Which platform do you create content on? (YouTube, Instagram, etc.) "
            )

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        response = "Thanks! Our team will reach out to you shortly."
        print(response)
        state["messages"].append(response)
        return state

    # Fallback
    response = "Sorry, I didn’t understand that. Could you rephrase?"
    print(response)
    state["messages"].append(response)
    return state


def build_graph():
    graph = StateGraph(dict)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)
    return graph.compile()
