import datetime

class Record:
    def __init__(self, record_id):
        self.__record_id = record_id  # Private attribute
        self.created_at = datetime.datetime.now()

    # Getter for private ID
    @property
    def record_id(self):
        return self.__record_id

    def get_details(self):
        return f"ID: {self.__record_id} | Created: {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Event(Record):
    def __init__(self, record_id, name, date):
        super().__init__(record_id)
        self.name = name
        self.date = date

    # Method Overriding
    def get_details(self):
        base_info = super().get_details()
        return f"[EVENT] {self.name} on {self.date} ({base_info})"

class Room(Record):
    def __init__(self, record_id, room_number, capacity):
        super().__init__(record_id)
        self.room_number = room_number
        self.capacity = capacity

    # Method Overriding
    def get_details(self):
        base_info = super().get_details()
        return f"[ROOM] {self.room_number} (Capacity: {self.capacity}) ({base_info})"

class Booking:
    def __init__(self, event, room):
        self.event = event
        self.room = room
        self.status = "Confirmed"
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Booking: {self.event.name} in Room {self.room.room_number} - Status: {self.status}"