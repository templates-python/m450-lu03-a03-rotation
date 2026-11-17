# M450 LU03.A03 - Rotation-Chiffre

Schreibe die Unittests für das Programm `main.py`.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu03/aufgaben/rotation>

## Ausgangslage

Die [Rotation-Chiffre](https://legacy.cryptool.org/de/cto/rotation) schreibt
den Klartext zeilenweise in Blöcke einer festen Länge, dreht diese Blöcke um
90° nach rechts und liest das Ergebnis wieder zeilenweise aus.

Beispiel mit der Blocklänge 5:

```text
Klartext:   kurzer Text  ->  KURZERTEXT

Blöcke:     K U R Z E        um 90° nach rechts gedreht:   R K
            R T E X T                                      T U
                                                           E R
                                                           X Z
                                                           T E

Chiffretext: RKTUERXZTE
```

In `main.py` ist das Programm fertig vorgegeben und in mehrere Funktionen
zerlegt. Es muss **nicht** verändert werden.

| Funktion | Verhalten |
| --- | --- |
| `prepare_text(text)` | entfernt Leerzeichen und wandelt in Grossbuchstaben um |
| `split_blocks(text, block_length)` | teilt den Text in Blöcke, der letzte Block wird mit `X` aufgefüllt |
| `rotate_right(blocks)` | dreht die Blöcke um 90° nach rechts |
| `encrypt(plaintext, block_length)` | verschlüsselt einen Klartext |
| `decrypt(ciphertext, block_length)` | entschlüsselt einen Chiffretext |

Die Docstrings beschreiben, wann welche Exception ausgelöst wird.

## Auftrag

In `main_test.py` sind die Testfunktionen vorbereitet. Die Kommentare
`# TODO ...` beschreiben jeweils, welche Situation zu testen ist. Teste für
jede Funktion

- gültige Werte,
- formal falsche Werte (falscher Datentyp), je ein Test pro Fehlersituation,
- formal korrekte, aber logisch ungültige Werte, je ein Test pro Fehlersituation.

Prüfe die Fehlersituationen mit `pytest.raises`.

## Lokal testen

```bash
pip install -r requirements.txt
pytest -v
python _run_pylint.py
```

## Bewertung

| Teil | Punkte |
| --- | --- |
| Unittests (15 Testfunktionen) | 15 |
| Linting von `main_test.py` | 3 |
| **Total** | **18** |

## Abgabe

Die Abgabe erfolgt durch den Push ins GitHub-Repository. Jeder Push wird
automatisch bewertet.
