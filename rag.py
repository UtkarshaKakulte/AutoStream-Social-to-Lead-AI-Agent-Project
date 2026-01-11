import json

with open("data/knowledge_base.json") as f:
    KB = json.load(f)

def fetch_knowledge(query):
    query = query.lower()

    if "price" in query or "plan" in query:
        return KB["pricing"]

    if "refund" in query or "support" in query:
        return KB["policies"]

    return "Sorry, I don't have that information."
