# TASKS M1.4 — Η κρεμάλα με χρώματα (pip)

Το τελευταίο βήμα του Module 1. Το `hangman.py` του repo σου παίρνει χρώματα με ένα πακέτο που έγραψαν άλλοι: το `rich`.

Κανόνες:
- Codespace, terminal.
- Οι ερωτήσεις με ✎ απαντιούνται στο `NOTES.md`, κάτω από `## M1.4`.
- **Ποτέ** Upload files από τη σελίδα του GitHub στο δικό σου repo. Όλα από το Codespace.

## Βήμα 0 — Checkpoint

`python hangman.py` → παίζει. Ένα γράμμα, `Ctrl + C`.

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

Στο `hangman.py`, κάτω από το `import random`: `from rich import print`

Μετά χρωμάτισε με markup `[χρώμα]...[/χρώμα]`:
- τον τίτλο «ΚΡΕΜΑΛΑ» έντονο κίτρινο (`bold yellow`)
- την κρεμάλα (`STAGES[...]`) κίτρινη, και στα δύο σημεία που τυπώνεται
- το «Σωστά!» έντονο πράσινο, το «Λάθος!» έντονο κόκκινο
- το «Μπράβο!» πράσινο, το «Κρεμάστηκες...» κόκκινο

Έλεγχος: `python hangman.py` → παίζεις με χρώματα.

✎ Τι έκανε η γραμμή `from rich import print` στο όνομα `print` του αρχείου σου;

## Βήμα 4 — requirements.txt

`pip freeze` → βρες τη γραμμή του rich.

Φτιάξε αρχείο `requirements.txt` στη ρίζα με μία γραμμή: `rich`

✎ Γιατί χρειάζεται αυτό το αρχείο, αφού το rich είναι ήδη εγκατεστημένο;

> Commit: `χρώματα με rich + requirements`

## Βήμα 5 (σπίτι) — Απόδειξη

`pip uninstall rich` (πάτα `y`) → `python hangman.py` → τι σφάλμα;

`pip install -r requirements.txt` → `python hangman.py` → δουλεύει;

✎ Πότε θα χρειαστείς την εντολή `pip install -r requirements.txt` στην πράξη;

## Βήμα 6 (σπίτι) — Οι υπόλοιπες εντολές

Τρέξε καθεμία και γράψε σε μία γραμμή τι κάνει:

- `pip install -U rich`
- `pip install rich==13.0.0` → `pip show rich` → τι άλλαξε στο `Requires`;
- `pip install -U rich` (πίσω στη νεότερη)
- `pip help install`

✎ Τι κάνει το `-U`; Τι κάνει το `--user`; (το δεύτερο από το `pip help install`, χωρίς να το τρέξεις)

Άνοιξε στον browser `https://pypi.org/project/rich/`.

✎ Ποια είναι η πιο πρόσφατη έκδοση του rich στο PyPI; Είναι ίδια με τη δική σου;

## Bonus

Το `rich` έχει και πίνακες. Στο τέλος του παιχνιδιού τύπωσε έναν πίνακα με δύο στήλες: «Γράμμα» και «Σωστό/Λάθος», για κάθε γράμμα που μάντεψες. Ξεκίνα από εδώ: `https://rich.readthedocs.io/en/stable/tables.html`
