from models.event import Event
from services.scheduler import Scheduler
from utils.stats import generate_report


def main():
    sess = Scheduler()

    while True:
        print("\n--- SESS: Smart Event Scheduler ---")
        print("1. Add Event")
        print("2. View Schedule & Stats")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == '1':
            name = input("Event Name: ")
            room = input("Room ID: ")
            start = int(input("Start Time (24h format): "))
            end = int(input("End Time (24h format): "))

            new_event = Event(name, start, end, room)
            if sess.add_booking(new_event):
                print("✅ Booking Successful!")
            else:
                print("❌ Conflict Detected! Room already booked.")

        elif choice == '2':
            generate_report(sess.bookings)

        elif choice == '3':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()