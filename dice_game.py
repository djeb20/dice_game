import numpy as np

"""
Simulating a one player version of the french dice game.
"""

class Dice_game:

    def __init__(self):

        pass

    def reset(self):
        """
        A reset plays a random 6 dice roll
        """

        self.s = np.random.randint(1, 7, 6)

        return self.s

    def step(self, action):
        """
        The available actions are taking out any single dice, stopping or rerolling the rest.
        action in {0, ..., 7}
        """

        if action == 7: # Chosen to stick and game ends
            pass
        elif action == 6: # Chosen to reroll rest of dice
            pass
        else: # Chosen to bank some dice


