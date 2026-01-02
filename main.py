import json, random

Emotes = json.load(open("Emotes.json", encoding="utf-8"))
RandomEmote = random.choice(Emotes)

for Index, Value in RandomEmote.items():
    print(f"{Index}: {Value}")
