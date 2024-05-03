import pickle
import random
import os

import numpy as np


def get_answer():
    user_answer = []
    print("Enter your answer. (Press Enter to add new row and Separate the numbers with space)\n"
          "Enter \"Q\" to exit input when your are finished")
    while True:
        user_input = input()
        if user_input.title() == 'Q':
            break
        user_answer.append([int(num) for num in user_input.split(" ")])

    return user_answer


def dot_product_game(file1, file2):
    score = 0

    array1 = random.choice(file1)
    array2 = random.choice(file2)

    print("Calculate dot product of the following arrays: ")

    print(f"{array1} \n\n {array2}")

    correct_answer = np.dot(array1, array2)
    # print(correct_answer)
    user_answer = np.array(get_answer())

    if np.array_equal(correct_answer, user_answer):
        print("Correct Answer!!")
        score = 1
    else:
        print("Wrong Answer!!")
        print(f"Your answer: \n{user_answer}")
        print(f"Correct answer: \n{correct_answer}")
        score = 0

    return score


def save_user_score(name: str, score: int):
    user_scores = {}

    # Check if file exists and is not empty
    if os.path.exists("player_info.pkl") and os.path.getsize("player_info.pkl") > 0:
        with open("player_info.pkl", "rb") as f:
            # Load the existing data
            try:
                user_scores = pickle.load(f)
            except EOFError:
                # File is empty, no loading to do
                user_scores = {}

    # Update the user score or add a new entry
    user_scores[name] = score

    # Save back to the file
    with open("player_info.pkl", "wb") as f:
        pickle.dump(user_scores, f)

    print(f"{name}, Your score has been saved")


def load_user_scores():
    try:
        with open("player_info.pkl", "rb") as f:
            user_scores = pickle.load(f)
            print(user_scores)
    except (EOFError, FileNotFoundError):
        print("No scores available.")


if __name__ == '__main__':
    choice = input("Press 1 to play the game\n"
                   "Press 2 to load the score\n")
    if choice == '1':
        file1_array = np.load("file1.npy")
        file2_array = np.load("file2.npy")
        rounds = 5
        points = 0
        user = input("Enter your name: ")
        print(f"Hello {user}. Welcome to Dot Product Game\n"
              f"There will be {rounds} rounds. Be prepared!!")
        for x in range(rounds):
            points += dot_product_game(file1_array, file2_array)
        save_user_score(user, points)

    elif choice == '2':
        load_user_scores()

    else:
        print("Invalid input\nExiting...")

