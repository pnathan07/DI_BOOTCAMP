from game import Game

def get_user_menu_choice():
    choices = ['Play a new game', 'Show scores', 'Quit']
    print("Menu:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    choice = input("Enter your choice: ").strip().lower()
    
    if choice in ['1', 'play a new game']:
        return 'play'
    elif choice in ['2', 'show scores']:
        return 'scores'
    elif choice in ['3', 'quit']:
        return 'quit'
    else:
        print("Invalid choice. Please try again.")
        return get_user_menu_choice()

def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThank you for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == 'play':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 'scores':
            print_results(results)
        elif choice == 'quit':
            print_results(results)
            break

if __name__ == "__main__":
    main()
