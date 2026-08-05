import random

posture = random.choice(["sitting", "standing"])
direction = random.choice(["left", "right", "facing"])
distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance: {distance}")
if posture == "sitting":
    print("Nexus stands up")
elif posture == "standing":
    pass
if direction in ["left","right"]:
    print("Nexus turns towards the door")
elif direction == "facing":
    pass
while distance>0:
    print(f"Moving {distance} steps left")
    distance-=1

print("Door Reached")