events = []

while True:
    print("\n1. Add Event")
    print("2. View Events")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter Title: ")
        date = input("Enter Date: ")
        events.append({"title": title, "date": date})
        print("Event Added Successfully!")

    elif choice == "2":
        for event in events:
            print(event)

    elif choice == "3":
        break
