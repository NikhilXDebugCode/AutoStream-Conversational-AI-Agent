from app.rag import rag_answer

print("Type 'exit' to stop")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break

    if any(word in user_input.lower() for word in ["hi", "hello", "hey"]):
        print("Hello! How can I help you today?")
        continue

    response = rag_answer(user_input)
    print(response)
