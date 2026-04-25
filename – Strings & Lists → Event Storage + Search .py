events = []

def add_event():
    title = input("Title: ")
    department = input("Department: ")
    events.append({"title": title, "department": department})

def search_event():
    keyword = input("Search Title: ").lower()
    for event in events:
        if keyword in event["title"].lower():
            print(event)

while True:
    print("\n1.Add 2.Search 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_event()
    elif ch == "2":
        search_event()
    else:
        break