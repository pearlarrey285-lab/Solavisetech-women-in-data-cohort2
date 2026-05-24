print("--- Favorite Tools List ---")
tools = ["Hammer", "Wrench", "Screwdriver"]
print(f"Original list: {tools}")

tools.append("Pliers")
print(f"After adding Pliers: {tools}")

tools.remove("Wrench")
print(f"After removing Wrench: {tools}")

print("\n--- Student Scores ---")
scores = [85, 92, 78, 90, 88]
print(f"All Scores: {scores}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Average Score: {sum(scores) / len(scores):.2f}")
