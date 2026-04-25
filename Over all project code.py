# Simple Smart Event & Space Scheduler (SESS)
# Stage: Basic CLI with Add / View / Search
# No files, no OOP – only lists, dicts, loops, and functions

import datetime

# Global list to store events
events = []  # each event is a dictionary


def validate_date(date_str):
    """Validate date in format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_time(time_str):
    """Validate time in format HH:MM (24-hour)."""
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def add_event():
    print("\n=== ADD NEW EVENT ===")
    name = input("Enter event name: ").strip()
    if not name:
        print("Event name cannot be empty.")
        return

    date = input("Enter event date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    start_time = input("Enter start time (HH:MM, 24-hour): ").strip()
    if not validate_time(start_time):
        print("Invalid start time format. Please use HH:MM.")
        return

    end_time = input("Enter end time (HH:MM, 24-hour): ").strip()
    if not validate_time(end_time):
        print("Invalid end time format. Please use HH:MM.")
        return

    venue = input("Enter venue/room name: ").strip()
    if not venue:
        print("Venue cannot be empty.")
        return

    department = input("Enter department (e.g., CSE, ECE): ").strip()
    event_type = input("Enter event type (lecture, seminar, workshop, etc.): ").strip()

    # Create event dictionary
    event = {
        "name": name,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "venue": venue,
        "department": department,
        "type": event_type
    }

    events.append(event)
    print("Event added successfully!")


def view_events():
    print("\n=== ALL SCHEDULED EVENTS ===")
    if not events:
        print("No events scheduled yet.")
        return

    # Header
    print(f"{'ID':<3} {'Name':<20} {'Date':<12} {'Start':<6} {'End':<6} {'Venue':<15} {'Dept':<8} {'Type':<10}")
    print("-" * 90)

    # Rows
    for idx, ev in enumerate(events, start=1):
        print(f"{idx:<3} {ev['name']:<20} {ev['date']:<12} {ev['start_time']:<6} {ev['end_time']:<6} "
              f"{ev['venue']:<15} {ev['department']:<8} {ev['type']:<10}")


def search_events():
    print("\n=== SEARCH EVENTS ===")
    if not events:
        print("No events to search.")
        return

    keyword = input("Enter event name or department to search: ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []
    for ev in events:
        if keyword in ev["name"].lower() or keyword in ev["department"].lower():
            results.append(ev)

    if not results:
        print("No matching events found.")
        return

    print(f"\nFound {len(results)} matching event(s):")
    print(f"{'Name':<20} {'Date':<12} {'Start':<6} {'End':<6} {'Venue':<15} {'Dept':<8} {'Type':<10}")
    print("-" * 90)
    for ev in results:
        print(f"{ev['name']:<20} {ev['date']:<12} {ev['start_time']:<6} {ev['end_time']:<6} "
              f"{ev['venue']:<15} {ev['department']:<8} {ev['type']:<10}")


def main_menu():
    while True:
        print("\n========== SMART EVENT & SPACE SCHEDULER (SESS) ==========")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Search Events")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            search_events()
        elif choice == "4":
            print("Exiting SESS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()