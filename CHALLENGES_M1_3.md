# CHALLENGES M1.3 — Modules & πακέτα

Δουλεύεις σε νέο φάκελο `challenges_m1_3/` μέσα στο repo σου, **όχι** μέσα στο `hangman/`.

Σε κάθε πρόκληση: **πρώτα** γράφεις την πρόβλεψή σου στο `NOTES.md` (κάτω από `## Challenges M1.3`), **μετά** τρέχεις. Αν έπεσες έξω, γράφεις σε μία γραμμή γιατί.

---

## Πρόκληση 1 — Ποιος με τρέχει; (5')

Φτιάξε δύο αρχεία:

- `whoami.py`: τυπώνει το `__name__` του, και μετά «Με έτρεξαν απευθείας» ή «Με έκαναν import», ανάλογα με το πώς ξεκίνησε.
- `runner.py`: κάνει `import whoami` **δύο φορές** στη σειρά, και μετά τυπώνει το δικό του `__name__` και το `whoami.__name__`.

✎ **Πρόβλεψη:** Πόσες γραμμές θα τυπώσει το `python runner.py`; Τι ακριβώς;

Τρέξε `python whoami.py` και `python runner.py`.

---

## Πρόκληση 2 — Το πρώτο σου πακέτο (10')

Φτιάξε το πακέτο `geometry` με:

```
challenges_m1_3/
├─ main.py
└─ geometry/
   ├─ __init__.py      ← docstring μίας γραμμής
   ├─ circle.py        ← area(r), perimeter(r)
   └─ square.py        ← area(a)
```

Το `circle.py` τρέχει και μόνο του (με test μέσα σε `if __name__ == "__main__":`), χωρίς να τρέχει το test όταν γίνεται import.

Στο `main.py` χρησιμοποίησε **και τις τρεις** μορφές, από μία φορά την καθεμία:
- `import geometry.circle`
- `from geometry import square`
- `from geometry.circle import perimeter`

και τύπωσε το εμβαδόν κύκλου ακτίνας 2, το εμβαδόν τετραγώνου πλευράς 3 και την περίμετρο κύκλου ακτίνας 1 (όλα με 2 δεκαδικά, με `round`).

✎ **Πρόβλεψη:** Στο terminal, με νέο `python`:

```python
>>> import geometry
>>> geometry.square.area(2)
```

Τι θα γίνει; Και αν αμέσως μετά γράψεις `from geometry import square` και ξαναδοκιμάσεις `geometry.square.area(2)`;

---

## Πρόκληση 3 — Τι φέρνει το `import *`; (7')

Στο `circle.py`:
- πρόσθεσε docstring στο module και σε κάθε δημόσια συνάρτηση
- πρόσθεσε βοηθητική συνάρτηση `_check(r)` που σηκώνει `ValueError("αρνητική ακτίνα")` αν το `r` είναι αρνητικό· κάλεσέ τη μέσα στις `area` και `perimeter`

✎ **Πρόβλεψη:** Μετά από `from geometry.circle import *`, ποια ονόματα (που δεν αρχίζουν με `__`) υπάρχουν; Δουλεύει το `_check(-1)`;

Έλεγξε με:

```python
>>> from geometry.circle import *
>>> sorted(n for n in dir() if not n.startswith("__"))
```

Μετά, με νέο `python`: `import geometry.circle as c` → `c.area(-1)` → `help(c)`.

---

## Πρόκληση 4 — Πακέτο μέσα σε zip (8', ή στο σπίτι)

1. Από τον φάκελο `challenges_m1_3/`: `zip -r geo.zip geometry -x "*/__pycache__/*"`
2. Φτιάξε φάκελο `elsewhere/` και μέσα το `zip_main.py`, που:
   - προσθέτει το `"geo.zip"` στο `sys.path`
   - κάνει `from geometry import square`
   - τυπώνει `square.area(5)` και `square.__file__`

✎ **Πρόβλεψη:** Το `square.__file__` θα δείχνει στον φάκελο `geometry/` ή μέσα στο zip; Γιατί;

Τρέξε **με δύο τρόπους**:
- από τον `challenges_m1_3/`: `python elsewhere/zip_main.py`
- από τον `elsewhere/`: `cd elsewhere` και `python zip_main.py`

✎ Ο ένας τρόπος σπάει. Ποιος και γιατί;

---

> Commit στο τέλος: `challenges M1.3`
