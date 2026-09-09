# Κρεμάλα — PCAP 2026-27, Εβδομάδα 01
# Ένα απλό παιχνίδι σε terminal, επιπέδου PCEP.
# Τρέξε το με:  python hangman.py

import random

WORDS = ["python", "github", "codespace", "commit", "variable", "function"]
MAX_MISTAKES = 6

STAGES = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]


def pick_word():
    return random.choice(WORDS)


def show_word(word, guessed):
    # Δείχνει το γράμμα αν έχει βρεθεί, αλλιώς παύλα.
    result = ""
    for letter in word:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def word_complete(word, guessed):
    # True αν όλα τα γράμματα της λέξης έχουν βρεθεί.
    for letter in word:
        if letter not in guessed:
            return False
    return True


def play():
    word = pick_word()
    guessed = []
    mistakes = 0

    print("=" * 30)
    print("   ΚΡΕΜΑΛΑ")
    print("=" * 30)

    while mistakes < MAX_MISTAKES:
        print(STAGES[mistakes])
        print(show_word(word, guessed))
        guess = input("Γράμμα: ").lower()

        if guess in guessed:
            print("Το έχεις ήδη πει!")
            continue

        guessed.append(guess)

        if guess in word:
            print("Σωστά!")
        else:
            mistakes += 1
            print("Λάθος!")

        if word_complete(word, guessed):
            print()
            print("Μπράβο! Η λέξη ήταν:", word)
            return True

    print(STAGES[mistakes])
    print("Κρεμάστηκες... Η λέξη ήταν:", word)
    return False


play()
