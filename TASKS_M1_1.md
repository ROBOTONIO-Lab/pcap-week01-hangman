# Project · Βήμα 1 (M1.1): Η κρεμάλα σπάει σε modules

Ξεκινάς από το `hangman.py` της προηγούμενης εβδομάδας (με τα tasks που έχεις κάνει). Στο τέλος θα έχεις **3 αρχεία** που συνεργάζονται. Το παιχνίδι πρέπει να τρέχει κανονικά μετά από **κάθε** task.

Κανόνας: 1 task = 1 commit = 1 sync. Μήνυμα: `m1.1 task N: …`

## Task 1 — words.py

1. Φτιάξε αρχείο `words.py`. Μετέφερε εκεί το `import random`, τη λίστα `WORDS` και τη συνάρτηση `pick_word()`.
2. Μετονόμασε το `hangman.py` σε `game.py` (δεξί κλικ → Rename).
3. Στην αρχή του `game.py` βάλε `import words`.
4. Βρες πού καλείται η `pick_word()` και άλλαξέ την σε `words.pick_word()`.
5. Τρέξε `python game.py`. Δουλεύει;

> Commit: `m1.1 task 1: words.py`

## Task 2 — art.py

1. Φτιάξε αρχείο `art.py`. Μετέφερε εκεί τη λίστα `STAGES`.
2. Στο `game.py`: `from art import STAGES`.
3. Το `STAGES[mistakes]` μένει όπως είναι — γιατί δεν χρειάζεται `art.`;

> Commit: `m1.1 task 2: art.py`

## Task 3 — Alias

1. Άλλαξε το `import words` σε `import words as w`.
2. Το πρόγραμμα σκάει. Πού; Διόρθωσέ το.
3. Ερώτηση στο `NOTES.md`: μετά το `as w`, υπάρχει ακόμα το όνομα `words` στο `game.py`;

> Commit: `m1.1 task 3: alias`

## Task 4 — Το * (και γιατί όχι)

1. Άλλαξε προσωρινά σε `from words import *` και κάλεσε `pick_word()` σκέτο. Δουλεύει;
2. Πρόσθεσε στο τέλος του `game.py` τη γραμμή `print(random)`. Τρέξε. Τι βλέπεις και ΠΟΥ βρέθηκε το `random` στο `game.py`;
3. Γύρνα στη μορφή που προτιμάς (`import words` ή `from words import pick_word`) και γράψε στο `NOTES.md` σε 2 γραμμές γιατί το `*` είναι κακή ιδέα.

> Commit: `m1.1 task 4: no star`

## Task 5 — Καθαριότητα

1. Σβήσε τη γραμμή `print(random)` αν έμεινε.
2. Βεβαιώσου ότι το `game.py` ξεκινά με τα import και ότι κάθε module έχει ένα σχόλιο στην πρώτη γραμμή που λέει τι περιέχει.
3. Τελικό commit + sync. Στο github.com πρέπει να βλέπεις: `art.py`, `game.py`, `words.py`, `TASKS.md`, `NOTES.md`.

> Commit: `m1.1 task 5: cleanup`

---
Στο φάκελο υπάρχει και ένας φάκελος `__pycache__`. Μην τον σβήσεις — θα μάθουμε τι είναι στο μάθημα 1.3. (Το `.gitignore` φροντίζει να μην ανεβαίνει στο GitHub.)
