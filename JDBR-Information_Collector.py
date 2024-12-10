"""
Project: PythonProject
program: Collect Information from the User
Purpose: Track information from the Rock, Paper, Scissors game based on the names of the teams/users
Revision History:
    Created on November 26th, 2024. By Juan (David) Barrios Rozo
    edited on December 2nd, 2024, by Juan (David) Barrios Rozo
    edited on December 3rd, 2024, by Juan (David) Barrios Rozo
    edited on December 4th, 2024, by Juan (David) Barrios Rozo
    edited on December 5th, 2024, by Juan (David) Barrios Rozo

"""

import sys # import sys gives access to the program to some parameters/functions. In the context of this program if only for the sys.exit message
import random #import random add randomness to Python's choices when playing RPS
from enum import Enum

# Global list to store Player objects
players = []


# The following player class intention is to track the user with their name, games played and points won in each game
class Player:
    team_name = input("Please enter your team's name: ")
    print(f"Welcome {team_name} to the Rock, Paper, Scissors Game!")
    total_players = 0

    def __init__(self, name, games_played, points=0):
        self.name = name
        self.games_played = games_played
        self.__points = points  # Private attribute
        Player.total_players += 1

    def add_points(self, points):
        if points < 0:
            raise ValueError("Points to add must be a positive integer.")
        self.__points += points

    def display_info(self):
        return f"Name: {self.name}, Games Played: {self.games_played}, Points: {self.__points}"
    # Return the information provided by the user on the team_name
    @staticmethod
    def display_team_name():
        return f"Team Name: {Player.team_name}"

# RPS Game
def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    user_wins = 0
    python_wins = 0
    game_count = 0

    while True:
        try:
            print("\nEnter: \n1 for Rock, \n2 for Paper, \n3 for Scissors")
            player_choice = int(input("Your choice: "))
            if player_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please choose 1, 2, or 3.")

            python_choice = random.choice([1, 2, 3])

            print(f"You chose {RPS(player_choice).name}.")
            print(f"Python chose {RPS(python_choice).name}.")

            if player_choice == python_choice:
                print("😯 It's a tie!")
            elif (player_choice == 1 and python_choice == 3) or \
                    (player_choice == 2 and python_choice == 1) or \
                    (player_choice == 3 and python_choice == 2):
                print("🎉 You win!")
                user_wins += 1
            else:
                print("🐍 Python wins!")
                python_wins += 1

            game_count += 1

            print(f"\nTotal Games: {game_count}")
            print(f"Your Wins: {user_wins}, Python Wins: {python_wins}")

            continue_playing = input("\nPlay again? (Y to continue, Q to quit): ").lower()
            if continue_playing == 'q':
                break

        except ValueError as e:
            print(f"Error: Enter a positive integer. Please try again. {e}")

    # This table will display the results of the game once the user quits
    print("\nFinal Scores:")
    print(f"Total Games Played: {game_count}")
    print(f"Your Wins: {user_wins}")
    print(f"Python Wins: {python_wins}")

# This function will allow the user to add a new player every time the user selects 1.
def add_player():
    try:
        name = str(input("Enter player's name: ")).strip()
        if not name and int:
            raise ValueError("Name cannot be blank or contain any numerical value. Please, enter a valid name.")

        games_played = int(input("Enter games played: "))
        if games_played < 0:
            raise ValueError("Games played cannot be negative. Please enter a positive integer")

        points = int(input("Enter points: "))
        if points < 0:
            raise ValueError("Points cannot be negative. Please enter a positive integer")

        player = Player(name, games_played, points)
        players.append(player)
        print(f"Player '{name}' added successfully!")
    except ValueError as e:
        print(f"Error: Invalid input. Please try again {e}")

# This function allows the user to add points to the player's total
def add_points():
    try:
        name = str(input("Enter player's name to add points: ")).strip()
        player = next((p for p in players if p.name == name), None)

        if not player:
            raise ValueError("Player not found. Please try again.")

        points = int(input("Enter points to add: "))
        if points < 0:
            raise ValueError("Points must be a positive integer.")

        player.add_points(points)
        print(f"Points added to {player.name} successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# Function to edit an existing player's details
def edit_existing_player():
    try:
        name = input("Enter the player's name to edit: ").strip()
        player = next((p for p in players if p.name == name), None)

        if not player:
            raise ValueError("Player not found.")

        print("\nWhat would you like to edit?")
        print("1. Name")
        print("2. Games Played")
        print("3. Points")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_name = str(input("Enter the new name: ")).strip()
            if not new_name or int:
                raise ValueError("Name cannot be blank or contained numerical value.")
            player.name = new_name
            print(f"Player's name updated to '{new_name}'.")
        elif choice == 2:
            new_games_played = int(input("Enter the new number of games played: "))
            if new_games_played < 0:
                raise ValueError("Games played cannot be negative.")
            player.games_played = new_games_played
            print(f"Player's games played updated to {new_games_played}.")
        elif choice == 3:
            new_points = int(input("Enter the new points: "))
            if new_points < 0:
                raise ValueError("Points cannot be negative.")
            player.add_points(new_points - player._Player__points)  # Adjust points
            print(f"Player's points updated to {new_points}.")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError as e:
        print(f"Error: Invalid input {e}. Please enter a valid player name.")

# This function will allow the user to remove players from the team
def remove_existing_player():
    try:
        name = input("Enter the player's name to remove: ").strip()
        player = next((p for p in players if p.name == name), None)

        if not player:
            raise ValueError("Player not found. Please enter a valid name.")

        players.remove(player)
        print(f"Player '{name}' has been removed successfully.")
    except ValueError as e:
        print(f"Error: {e}")

"""The content of this function is implicit withing the edit_existing_player function"""
# # This function will help the user to remove points from a player
# def remove_points():
#     try:
#         name = input("Enter the player's name to remove points from: ").strip()
#         player = next((p for p in players if p.name == name), None)
#
#         if not player:
#             raise ValueError("Player not found.")
#
#         points_to_remove = int(input("Enter the number of points to remove: "))
#         if points_to_remove < 0:
#             raise ValueError("Points to remove cannot be negative.")
#
#         if points_to_remove > player._Player__points:
#             raise ValueError("Cannot remove more points than the player currently has and Points cannot be negative.")
#
#         player.add_points(-points_to_remove)  # Remove/Subtract points from the player
#         print(f"{points_to_remove} points removed from '{player.name}'. Total points: {player._Player__points}")
#     except ValueError as e:
#         print(f"Error: {e}")
"""The content of this function is implicit withing the edit_existing_player function"""
# # This function will allow the user to reset games played
# def reset_games_played():
#     try:
#         name = input("Enter the player's name to reset games played: ").strip()
#         player = next((p for p in players if p.name == name), None)
#
#         if not player:
#             raise ValueError("Player not found.")
#
#         player.games_played = 0
#         print(f"Games played for '{player.name}' has been reset to 0.")
#     except ValueError as e:
#         print(f"Error: {e}")

# This function will display all the players
def display_all_players():
    print(Player.display_team_name())
    print(f"Total Players: {Player.total_players}")
    for player in players:
        print(player.display_info())

# This function purpose is to display a copyright message after every action
def display_copyright():
    print("\u00A9 2024 Juan (David) Barrios Rozo. All rights are reserved. \n")

# This function contains the main menu where the user has to choose an option
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add Player")
        print("2. Add Points")
        print("3. Remove player from team")
        print("4. Display All Players")
        print("5. Play Rock-Paper-Scissors")
        print("6. Edit Player")
        print("7. Exit")

        # Raise value errors if the inputs from the user are incorrect
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_player()
                display_copyright()
            elif choice == 2:
                add_points()
                display_copyright()
            elif choice == 3:
                remove_existing_player()
                display_copyright()
            elif choice == 4:
                display_all_players()
                display_copyright()
            elif choice == 5:
                play_rps()
                display_copyright()
            elif choice == 6:
                edit_existing_player()
                display_copyright()
            elif choice == 7:
                print('\n🥳🥳🥳🥳')
                print('Thank you for playing!\n')
                sys.exit("Bye!👋")
                display_copyright()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid number between 1 and 5.")

# Execute the program
main_menu()
