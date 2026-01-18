class EscalationAgent:
    def summarize(self, conversation):
        summary = "Conversation Summary:\n"
        for msg in conversation:
            summary += f"- {msg}\n"
        return summary
