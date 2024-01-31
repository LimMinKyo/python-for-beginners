player = {"name": "ian", "age": 26, "alive": True, "fav_food": ["🍔", "🍕"]}

player["xp"] = 1500
player["fav_food"].append("🍜")

print(player.get("age"))
print(player["fav_food"])

print(player)
