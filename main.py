import datetime
import random
import json


def play():
    secret = random.randint(1, 99)
    attempts = 0
    player = input("What's your name? ")
    wrong_guesses = []
    data_list = get_data_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 99): "))
        attempts += 1

        if guess == secret:
            data_list.append({"attempts": attempts, "player_name": player, "secret_number": secret, "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})

            with open("data_list.json", "w") as data_file:
                data_file.write(json.dumps(data_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append({"wrong_guesses": guess})

def get_data_list():
    with open("data_list.json", "r") as data_file:
        data_list = json.loads(data_file.read())
        return data_list

def get_top_scores():
    data_list = get_data_list()
    ordered_list = sorted(data_list, key=lambda x: x["attempts"])[:3]
    return ordered_list

for data_dict in get_top_scores():
    results = "Player {0} guessed correctly it was number {1} in {2} tries on {3}.The wrong guesses were {4}."\
        .format(data_dict.get("player_name"),
                data_dict.get("secret_number"),
                str(data_dict.get("attempts")),
                str(data_dict.get("date")),
                data_dict.get("wrong_guesses"))
    print(results)

while True:
    play_again = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if play_again.upper() == "A":
        play()
    elif play_again.upper() == "B":
        for score_dict in get_top_scores():
            print(results)
    else:
        break
