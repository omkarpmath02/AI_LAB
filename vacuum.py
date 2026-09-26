# Vacuum Cleaner Agent with User Input

# Get room status from user
room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()

# Get starting position
current_room = input("Enter starting room (A/B): ").upper()

# Store rooms
rooms = {
    "A": room_A,
    "B": room_B
}

print("\n--- Vacuum Cleaner Agent ---")

while True:
    print("\nCurrent Room:", current_room)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])

    # If current room is dirty, clean it
    if rooms[current_room] == "Dirty":
        print("Room is dirty.")
        print("Vacuum cleaner is cleaning...")
        rooms[current_room] = "Clean"
        print("Room cleaned successfully!")

    else:
        print("Room is already clean.")

    # Check if both rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean!")
        print("Vacuum cleaner stopped.")
        break

    # Move to the other room
    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

    print("Moving to Room", current_room)
