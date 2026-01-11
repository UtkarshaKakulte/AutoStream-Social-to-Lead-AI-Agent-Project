from intent import detect_intent
from rag import fetch_knowledge
from tools import mock_lead_capture

state = {"name": None, "email": None, "platform": None}

print("🚀 AutoStream AI Agent Started...\n")

while True:
    user_input = input("User: ")
    intent = detect_intent(user_input)

    if intent == "greeting":
        print("Agent: Hello! Ask me about AutoStream pricing or features.")

    elif intent == "pricing":
        data = fetch_knowledge(user_input)
        print("Agent: Here are our plans:")
        for k, v in data.items():
            print(f" - {k}: {v}")

    elif intent == "high_intent":
        print("Agent: Please share your name:")
        state["name"] = input("Name: ")

        print("Agent: Your email:")
        state["email"] = input("Email: ")

        print("Agent: Your creator platform:")
        state["platform"] = input("Platform: ")

        mock_lead_capture(state["name"], state["email"], state["platform"])
        break

    else:
        print("Agent: Could you please rephrase?")
