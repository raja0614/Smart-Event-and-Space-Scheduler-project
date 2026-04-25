events = []

def validate_time(start, end):
    return start < end

def add_event():
    title = input("Title: ")
    start = int(input("Start Hour: "))
    end = int(input("End Hour: "))

    if not validate_time(start, end):
        print("Invalid time!")
        return

    events.append({"title": title, "start": start, "end": end})
    print("Event Added!")

def view_events():
    for event in events:
        print(event)

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_event()
    elif ch == "2":
        view_events()
    else:
        break
