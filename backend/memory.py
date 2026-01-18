class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append(f"{role}: {message}")

    def get_context(self):
        return "\n".join(self.history)

    def get_all(self):
        return self.history
