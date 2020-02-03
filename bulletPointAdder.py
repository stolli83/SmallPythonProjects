#! python3
# bulletPointAdder.py - Fügt Wikipedia-Aufzählungszeichen zu Beginn jeder
# Zeile des Textes in der Zwischenablage hinzu.

import pyperclip
text = pyperclip.paste()

# Trennt Zeilen und fügt Sternchen hinzu
lines = text.split('\n')
for i in range(len(lines)):     # Durchläuft alle Indizes in der Liste "lines"
    lines[i] = '* ' + lines[i]  # Fügt Stern zu allen Strings in "lines" hinzu

text= '\n'.join(lines)

pyperclip.copy(text)
