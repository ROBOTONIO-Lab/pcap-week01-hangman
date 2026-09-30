# TASKS M1.3 — Η κρεμάλα γίνεται πακέτο

Σήμερα τα αρχεία μας μαθαίνουν να καταλαβαίνουν **ποιος τα τρέχει**, αποκτούν περιγραφή και μπαίνουν σε έναν φάκελο-πακέτο.

Κανόνες (ίδιοι με το M1.2):
- Ένα βήμα = ένα commit = ένα sync. Μήνυμα commit: αυτό που γράφει στο τέλος κάθε βήματος.
- Μετά από κάθε βήμα το πρόγραμμα **τρέχει**. Αν δεν τρέχει, δεν προχωράς.
- Απαντάς τις ερωτήσεις με ✎ στο `NOTES.md`, 1 γραμμή η καθεμία, κάτω από τίτλο `## M1.3`.

Στην τάξη: βήματα 0–7. Στο σπίτι: 8–9.

---

## Βήμα 0 — Checkpoint

`python game.py`: βλέπεις banner και μπορείς να πατήσεις `?` για βοήθεια; Αν όχι, ολοκλήρωσε πρώτα τα βήματα 9–10 του `TASKS_M1_2.md`.

## Βήμα 1 — Ποιος με τρέχει; (πείραμα, χωρίς commit)

Πρόσθεσε στο τέλος του `words.py`: `print("words.py →", __name__)`

Τρέξε `python words.py` και μετά `python game.py`. Σημείωσε τι τύπωσε κάθε φορά.

✎ Τι τιμή έχει το `__name__` όταν τρέχεις ένα αρχείο και τι όταν το κάνεις import;

Σβήσε τη γραμμή.

## Βήμα 2 — Το τεστ γυρίζει πίσω

Στο τέλος του `words.py` πρόσθεσε ένα μπλοκ που τρέχει **μόνο** όταν το αρχείο εκτελείται απευθείας. Μέσα: ένα τεστ για καθεμία από τις `pick_word`, `pick_words` και `hint`.

Έλεγχος: `python words.py` → 3 γραμμές. `python game.py` → καμία από αυτές.

Κάνε το ίδιο για την κλήση `main()` στο `game.py`.

Έλεγχος: στο terminal, `python` → `import game` → **δεν** ξεκινά παιχνίδι. Μετά `game.show_word("python", ["p", "o"])` → τι βγάζει;

✎ Τι θα γινόταν στο `import game` αν δεν είχες προστατέψει το `main()`;

> Commit: `__name__ guard σε words και game`

## Βήμα 3 — `__pycache__`

Τρέξε `ls __pycache__`.

✎ Ποια αρχεία `.pyc` υπάρχουν; Γιατί λείπει το `game`;

Σβήσε τον φάκελο (`rm -rf __pycache__`), τρέξε `python words.py`, και ξανά `ls`. Μετά τρέξε `python game.py` (Ctrl+C) και ξανά `ls`.

✎ Ποια από τις δύο εντολές ξαναέφτιαξε τον φάκελο;

Φτιάξε `.gitignore` ώστε το `__pycache__/` να μην ανεβαίνει στο GitHub.

> Commit: `.gitignore για __pycache__`

## Βήμα 4 — Docstrings

Γράψε docstring μίας γραμμής:
- για ολόκληρο το `words.py`
- για τη συνάρτηση `hint`

Έλεγχος στο terminal: `import words` → `print(words.__doc__)` → `help(words.hint)` (`q` για έξοδο).

Δοκίμασε: μετακίνησε το docstring του αρχείου **κάτω** από το `import random` και ξανακοίτα το `words.__doc__` (χρειάζεται νέο `python`). Γύρισέ το πίσω.

✎ Πού πρέπει να βρίσκεται το docstring ενός module για να «μετράει»;

> Commit: `docstrings στο words`

## Βήμα 5 — Όνομα με `_`

Χώρισε την `hint` σε δύο συναρτήσεις: μία βοηθητική `_missing_letters(word, guessed)` που επιστρέφει τη λίστα με τα γράμματα που λείπουν (χωρίς διπλά), και την `hint` που διαλέγει ένα από αυτά.

Έλεγχος: `python words.py` → το τεστ του βήματος 2 δουλεύει ακόμα.

Στο terminal: `from words import *` και μετά δοκίμασε `pick_word()`, `_missing_letters("function", [])` και `random.random()`.

✎ Ποιο από τα τρία απέτυχε και γιατί; Ποιο πέτυχε ενώ δεν το περίμενες;

Νέο `python`: `import words` → `words._missing_letters("function", [])`.

✎ Αφού δουλεύει, τι σημαίνει τελικά το `_` μπροστά από ένα όνομα;

> Commit: `_missing_letters ως βοηθητική`

## Βήμα 6 — Πακέτο `hangman`

Φτιάξε φάκελο `hangman` και μετακίνησε μέσα τα `words.py`, `art.py`, `banner.py`. Το `game.py` μένει έξω.

Τρέξε `python game.py`.

✎ Τι σφάλμα βγήκε και γιατί;

Διόρθωσε τα imports του `game.py` ώστε να φέρνουν τα modules **από το πακέτο**. Χρειάζονται 2 γραμμές.

Πρόσθεσε `hangman/__init__.py` με ένα docstring μίας γραμμής για το πακέτο.

Έλεγχος: `python game.py` → παίζει. `python hangman/words.py` → το τεστ τρέχει.

> Commit: `πακέτο hangman`

## Βήμα 7 — Το `__init__.py` και οι μορφές import

Πρόσθεσε **προσωρινά** στο `__init__.py`: `print("__init__.py τρέχει:", __name__)`

✎ Πόσες φορές εμφανίζεται όταν τρέχεις `python game.py`; Γιατί τόσες;

Στο terminal δοκίμασε, με νέο `python` κάθε φορά:
1. `import hangman` → `hangman.words`
2. `import hangman.art` → `hangman.art.STAGES[1]`
3. `from hangman import words` → `'hangman' in dir()`

✎ Γιατί απέτυχε το (1);

Σβήσε το `print` από το `__init__.py`.

> Commit: `__init__.py με docstring`

---

## Βήμα 8 (σπίτι) — `sys.path` (πείραμα, χωρίς commit)

Φτιάξε φάκελο `scripts` και μετακίνησε μέσα το `game.py`. Τρέξε `python scripts/game.py`.

Πρόσθεσε στην κορυφή του `game.py` δύο γραμμές που τυπώνουν το πρώτο στοιχείο του `sys.path`.

✎ Ποιον φάκελο τύπωσε; Γιατί η Python δεν βρίσκει το `hangman`;

Αντικατάστησε το `print` με `sys.path.append("..")`. Τρέξε με δύο τρόπους:
- `cd scripts` και `python game.py`
- από τη ρίζα του repo: `python scripts/game.py`

✎ Ο ένας τρόπος δουλεύει και ο άλλος όχι. Γιατί;

**Αναίρεσε τα πάντα:** `game.py` πίσω στη ρίζα, σβήσε τις γραμμές με το `sys`, σβήσε τον φάκελο `scripts`. `python game.py` → παίζει.

## Βήμα 9 (σπίτι) — Shebang

Πρόσθεσε ως **πρώτη** γραμμή του `game.py` το shebang για Python 3. Στο terminal: `chmod +x game.py` και `./game.py`.

✎ Για ποιον γράφεται αυτή η γραμμή: για την Python ή για το λειτουργικό;

> Commit: `shebang`

---

## Τελική κατάσταση

```
.gitignore
game.py
hangman/
    __init__.py
    art.py
    banner.py
    words.py
NOTES.md
```

## Bonus

Γράψε docstring μίας γραμμής σε **κάθε** συνάρτηση του `game.py` και σε κάθε αρχείο του πακέτου. Μετά: `python` → `import game` → `help(game)`. Τι βλέπεις;
