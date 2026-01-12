def detect_intent(text: str) -> str:
    text = text.lower()

    if any(greet in text for greet in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    if any(word in text for word in ["buy", "sign up", "subscribe", "try", "pro plan"]):
        return "high_intent"

    return "unknown"
