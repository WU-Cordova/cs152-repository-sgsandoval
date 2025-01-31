import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        """ Constructor for the Game class. Sets the players to instance variables.
        Args:   
            player1 (Character): The first player.
            player2 (Character): The second player.
        """
        self.__player1 = player1
        self.__player2 = player2
        pass

    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        """
        random_roll = random.randint(1,6) # choses random number 1-6
        attack_power = random_roll * attacker.attack_power # multiplies attack power by that random number
        new_health = defender.health - attack_power # subtracts the attack number from defenders health
        # If statement: if defender health <= 0, end game and show message "defender defeated", else: keep going
        if new_health <= 0:
            print("defender defeated")
        else:
            pass

    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """

        pass