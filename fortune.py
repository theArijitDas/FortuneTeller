# fortune.py (v1.0)

print("🔮 Welcome to Arijit Das's Fortune Teller (21JE0157) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ")

if mood.lower() == "happy":
    print("✨ Your fortune: Great things await you, Arijit! Keep smiling. ✨")
elif mood.lower() == "sad":
    print("✨ Your fortune: Tough times don’t last, but tough people like you do. ✨")
elif mood.lower() == "neutral":
    print("✨ Your fortune: A calm mind opens doors to new beginnings. ✨")
else:
    print("✨ Your fortune: Mood unclear, but surprises are coming your way! ✨")
