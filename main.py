import json, random

Emotes = json.load(open("Emotes.json", encoding="utf-8"))

TotalEmotes = len(Emotes)
UniqueCreators = len(set(Emote["CreatorId"] for Emote in Emotes))

print(f"Total Emotes: {TotalEmotes}")
print(f"Unique Creators: {UniqueCreators}\n")
print("-" * 50, "\n")

RandomEmote = random.choice(Emotes)

for Index, Value in RandomEmote.items():
    print(f"{Index}: {Value}")