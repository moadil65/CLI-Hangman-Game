import random

hangman_stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """
]

wordbank = [
    "python", "laptop", "server", "github", "docker",
    "binary", "script", "cookie", "router", "debug",
    "syntax", "module", "cache", "kernel", "update",
    "system", "backup", "memory", "widget", "google"
    "youth", "vscode"
]

word = random.choice(wordbank)
word_to_guess = ["_"] * len(word)

wrong_guesses = 0
max_wrong = len(hangman_stages) - 1

print("Welcome to Hangman!")
while wrong_guesses < max_wrong and '_' in word_to_guess:
    print(hangman_stages[wrong_guesses])
    print("Current word:", " ".join(word_to_guess))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        found = False
    
        for i in range(len(word)):
            if word[i] == guess and word_to_guess[i] == "_":
                word_to_guess[i] = guess
                found = True
    
        if not found:
            print("You already guessed that letter in the correct place.")
        else:
            print("Great guess!")
    
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong - wrong_guesses}")

if "_" not in word_to_guess:
    print("Congratulations! You guessed the word:", word)

else:
    print(hangman_stages[wrong_guesses])
    print("Sorry, you failed to guess the word. It was:", word)
