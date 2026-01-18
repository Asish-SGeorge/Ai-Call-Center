class PrimaryAgent:
    def __init__(self, model):
        self.model = model

    def respond(self, user_input, context):
        prompt = f"""
You are a professional AI call center agent.

Rules:
- Be polite and concise
- Ask clarifying questions if needed
- Do NOT assume missing details
- Calm frustrated users

Conversation so far:
{context}

Customer:
{user_input}
"""
        response = self.model.generate_content(prompt)
        return response.text
