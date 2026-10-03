words = ["python", "AI", "security", "code", "data", "network"]
langer_than_4 = [word for word in words if len(word) > 4]
sorteder_langer_than_4 = sorted(langer_than_4,key=len)
print("Words longer than 4 characters:", sorteder_langer_than_4)