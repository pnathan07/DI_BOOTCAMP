import random

class Game:
    def get_user_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        user_item = None

        while user_item not in valid_items:
            user_item = input("Please choose an item (rock, paper, scissors): ").strip().lower()
            if user_item not in valid_items:
                print("Invalid choice. Please select either 'rock', 'paper', or 'scissors'.")

        return user_item

    def get_computer_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        computer_item = random.choice(valid_items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'scissors' and computer_item == 'paper') or \
             (user_item == 'paper' and computer_item == 'rock'):
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        if result == 'win':
            print(f"You selected {user_item}. The computer selected {computer_item}. You win!")
        elif result == 'draw':
            print(f"You selected {user_item}. The computer selected {computer_item}. It's a draw!")
        else:
            print(f"You selected {user_item}. The computer selected {computer_item}. You lose!")

        return result
