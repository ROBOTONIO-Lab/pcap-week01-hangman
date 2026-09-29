import random

WORDS = ["robotonio", "python", "github", "codespace", "commit", "variable", "function", "table", "playroom", "korydallos"]

def pick_word():
    var = 0
    return random.choice(WORDS)

# print(pick_word())