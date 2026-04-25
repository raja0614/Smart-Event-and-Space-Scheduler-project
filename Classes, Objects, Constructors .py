class Event:
    def __init__(self, event_id, title, date, start, end, department, event_type):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.start = start
        self.end = end
        self.department = department
        self.event_type = event_type

    def display(self):
        print(f"{self.event_id} | {self.title} | {self.date} | {self.start}-{self.end} | {self.department} | {self.event_type}")