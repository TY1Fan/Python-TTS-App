from backend.client import Client

class User(Client):

    def __init__(self):
        super().__init__()
    
    def get_usage(self):
        subscription = self.client.user.subscription.get()
        remainder = subscription.character_limit - subscription.character_count
        result = f"Character remaining: {remainder} characters"

        print(result)
        return result