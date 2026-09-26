# Vacuum Cleaner Agent with Obstacle and Wall Avoidance

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

    # Clean current room
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

    # Check for obstacle
    obstacle = input("\nIs there an obstacle in front? (Yes/No): ").capitalize()

    if obstacle == "Yes":

        print("Obstacle detected!")

        # Check left and right
        left_blocked = input("Is there a wall/obstacle on the LEFT? (Yes/No): ").capitalize()
        right_blocked = input("Is there a wall/obstacle on the RIGHT? (Yes/No): ").capitalize()

        if left_blocked == "No":
            print("Moving LEFT...")
            print("Obstacle avoided successfully!")

        elif right_blocked == "No":
            print("Moving RIGHT...")
            print("Obstacle avoided successfully!")

        else:
            print("LEFT and RIGHT are blocked!")
            print("Cannot move. Turning around...")
            print("Moving backwards.")

    else:
        print("No obstacle detected.")

    # Move to the other room
    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

    print("Moving to Room", current_room)
