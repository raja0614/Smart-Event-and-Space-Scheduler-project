

# models/room.py
class Room:
    def __init__(self, room_id, capacity, features):
        self.room_id = room_id
        self.capacity = capacity
        self.features = set(features)  # e.g., {"Projector", "Wi-Fi"}

# models/event.py
class Event:
    def __init__(self, name, start, end, room_id):
        self.name = name
        self.start = start  # Use integers for simplicity (e.g., 10 for 10 AM)
        self.end = end
        self.room_id = room_id



# services/scheduler.py
class Scheduler:
    def __init__(self):
        self.bookings = []

    def check_conflict(self, new_start, new_end, room_id):
        for b in self.bookings:
            if b.room_id == room_id:
                # Logic: (StartA < EndB) and (EndA > StartB)
                if new_start < b.end and new_end > b.start:
                    return True
        return False

    def add_booking(self, event):
        if not self.check_conflict(event.start, event.end, event.room_id):
            self.bookings.append(event)
            return True
        return False