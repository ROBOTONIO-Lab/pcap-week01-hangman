# TASKS M1.4 — Η κρεμάλα με χρώματα (pip)

Το τελευταίο βήμα του Module 1. Η κρεμάλα χρησιμοποιεί ένα πακέτο που έγραψαν άλλοι: το `rich`.

Κανόνες:
- Codespace, terminal.
- Οι ερωτήσεις με ✎ απαντιούνται στο `NOTES.md`, κάτω από `## M1.4`.
- **Ποτέ** Upload files από τη σελίδα του GitHub στο δικό σου repo. Όλα από το Codespace. Αν δούλεψες και αλλού, πρώτα Sync Changes.

## Βήμα 1 — Τι υπάρχει ήδη

Στο terminal: `pip --version`, μετά `pip list`.

✎ Πόσα πακέτα είναι εγκατεστημένα; Εσύ εγκατέστησες κάποιο;

`python -c "import rich"` → τι σφάλμα;

## Βήμα 2 — Εγκατάσταση

`pip install rich`

✎ Πόσα πακέτα κατέβηκαν; Γιατί περισσότερα από ένα;

`pip show rich`

✎ Ποια έκδοση έχεις; Τι γράφει η γραμμή `Requires`;

## Βήμα 3 — Χρώματα

Στο `game.py`, κάτω από τα άλλα import: `from rich import print`

Μετά χρωμάτισε με markup `[χρώμα]...[/χρώμα]`:
- την κρεμάλα (`STAGES[...]`) κίτρινη, και στα δύο σημεία που τυπώνεται
- το «Σωστά!» έντονο πράσινο (`bold green`)
- το «Λάθος!» έντονο κόκκινο
- το «Μπράβο!» πράσινο, το «Κρεμάστηκες...» κόκκινο

Έλεγχος: `python game.py` → παίζεις με χρώματα.

✎ Τι έκανε η γραμμή `from rich import print` στο όνομα `print` του αρχείου σου;

## Βήμα 4 — requirements.txt

`pip freeze` → βρες τη γραμμή του rich.

Φτιάξε αρχείο `requirements.txt` στη ρίζα με μία γραμμή: `rich`

✎ Γιατί χρειάζεται αυτό το αρχείο, αφού το rich είναι ήδη εγκατεστημένο;

> Commit: `χρώματα με rich + requirements`

## Βήμα 5 (σπίτι) — Απόδειξη

`pip uninstall rich` (πάτα `y`) → `python game.py` → τι σφάλμα;

`pip install -r requirements.txt` → `python game.py` → δουλεύει;

✎ Πότε θα χρειαστείς την εντολή `pip install -r requirements.txt` στην πράξη;

## Βήμα 6 (σπίτι) — Οι υπόλοιπες εντολές

Τρέξε καθεμία και γράψε σε μία γραμμή τι κάνει:

- `pip install -U rich`
- `pip help install`
- `pip list` μετά το uninstall και μετά το install ξανά (τι άλλαξε;)

✎ Τι κάνει το `-U`; Τι κάνει το `--user`; (το δεύτερο χωρίς να το τρέξεις· από το `pip help install`)

Άνοιξε στον browser `https://pypi.org/project/rich/`.

✎ Ποια είναι η πιο πρόσφατη έκδοση του rich στο PyPI; Είναι ίδια με τη δική σου;

## Τελική κατάσταση

```
.gitignore
game.py
requirements.txt
hangman/
NOTES.md
```

## Bonus

Το `rich` έχει και πίνακες. Στο τέλος της `main()`, αντί για το «Ποσοστό επιτυχίας», τύπωσε έναν πίνακα με στήλες «Γύρος», «Λέξη», «Αποτέλεσμα». Ξεκίνα από εδώ: `https://rich.readthedocs.io/en/stable/tables.html`
