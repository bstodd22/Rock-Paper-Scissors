import random


class RockPaperScissors:
    def __init__(self):
        self.user_points = 0
        self.computer_points = 0

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.user_points += 1
            self.computer_points += 1
            print("It's a tie!")
            print(
                f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
            )
        elif user_choice == "rock":
            if computer_choice == "scissors":
                self.user_points += 1
                print("You win!!")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
            else:
                self.computer_points += 1
                print("Computer wins!!")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
        elif user_choice == "paper":
            if computer_choice == "rock":
                self.user_points += 1
                print("You win!!")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
            else:
                self.computer_points += 1
                print("Computer wins")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
        elif user_choice == "scissors":
            if computer_choice == "paper":
                self.computer_points += 1
                print("Computer wins!!")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
            else:
                self.computer_points += 1
                print("Computer wins")
                print(
                    f"""User points: {self.user_points}
Computer points: {self.computer_points}"""
                )
        else:
            print("Invalid choice. Please try again.")

    def play(self):
        print("Welcome to Rock, Paper, Scissors!!")

        while True:
            user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

            choices = ["rock", "paper", "scissors"]
            computer_choice = random.choice(choices)

            if user_choice in choices:
                print(f"Computer choice: {computer_choice}")
                self.determine_winner(user_choice, computer_choice)
            else:
                print("Invalid choice. Please try again.")

            while True:
                play_again = input("Do you want to play again? (y/n): ")

                if play_again == "y":
                    break
                elif play_again == "n":
                    print("Thanks for playing!!")
                    print(
                        f"""Final Score:
User points: {self.user_points}
Computer points: {self.computer_points}"""
                    )
                    if self.user_points > self.computer_points:
                        print("You beat Computer!!")
                    elif self.user_points < self.computer_points:
                        print("Computer beat you!!")
                    elif self.user_points == self.computer_points:
                        print("You and computer tied!!")
                    return
                else:
                    print("Invalid.")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
