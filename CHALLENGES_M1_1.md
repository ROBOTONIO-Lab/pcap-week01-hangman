# Mini-challenges · M1.1 Modules & import

Δουλεύεις στο Codespace του `pcap-week01-hangman`. Φτιάξε φάκελο `challenges/` και ένα αρχείο ανά challenge. Στο τέλος: commit «m1.1 challenges».

## Challenge 1 — Ο μάντης (5')

Για ΚΑΘΕ απόσπασμα γράψε σε σχόλιο τι θα τυπώσει (ή `Error`) **πριν** το τρέξεις. Μετά τρέξ' το. Πόσα βρήκες;

```python
# α
import math
print(math.pi > 3)

# β
from math import pi
print(math.pi)

# γ
import math as m
print(m.floor(-2.5))

# δ
from math import floor as f
print(f(2.9), floor(2.9))
```

## Challenge 2 — Σπάσε το, φτιάξ' το (5')

Ο παρακάτω κώδικας σκάει. Διόρθωσέ τον με **τρεις διαφορετικούς τρόπους**, αλλάζοντας κάθε φορά μόνο ΜΙΑ γραμμή:

```python
import math as m
print(math.pi)
```

Ποιος από τους τρεις τρόπους είναι ο καλύτερος και γιατί;

## Challenge 3 — Namespace detective (5')

Γράψε πρόγραμμα που:
- ορίζει δική σου συνάρτηση `sqrt(x)` που επιστρέφει το string `"no idea"`,
- χρησιμοποιεί ΚΑΙ την πραγματική `sqrt` του `math`,
- τυπώνει `no idea 4.0` με μία `print`.

Ποια μορφή import ΔΕΝ μπορείς να χρησιμοποιήσεις εδώ; Γιατί;

## ★ Bonus — Δικό σου module (10')

1. Φτιάξε `greetings.py` με συνάρτηση `hello(name)` που επιστρέφει `"Γεια σου, <name>!"`.
2. Φτιάξε `main.py` που καλεί την `hello("Python")` **με τις 4 μορφές import**, μία μετά την άλλη, και τυπώνει 4 φορές τον χαιρετισμό.
3. Παρατήρησε τι εμφανίστηκε στον φάκελο μετά το τρέξιμο. Σημείωσέ το στο `NOTES.md`.
