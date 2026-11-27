
import random

class RandomAgent:

    def __init__(self):
        self.actions=["left","right","stay"]

    def choose_action(self, state):

        action = random.choice(self.actions)

        return action
