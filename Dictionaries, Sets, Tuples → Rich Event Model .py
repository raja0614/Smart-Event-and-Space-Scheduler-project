events = {}
event_types = set()
logs = []

def add_event():
    event_id = len(events) + 1
    title = input("Title: ")
    event_type = input("Type: ")

    events[event_id] = {
        "title": title,
        "type": event_type
    }

    event_types.add(event_type)
    logs.append((title, "CREATED"))

    print("Event Added!")

def view_events():
    for id, event in events.items():
        print(id, event)

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_event()
    elif ch == "2":
        view_events()
    else:
        break