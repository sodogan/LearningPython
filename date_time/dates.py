from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Get today's date
    today = date.today()
    print("Today's date is", today)
    print("Date components:", today.day, today.month, today.year)

    print("Today's weekday # is", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Whis is a:", days[today.weekday()])

    # Get current time and date
    today = datetime.now()
    print("The current date and time is", today)
    t = datetime.time(datetime.now())
    print("The time is", t)


if __name__ == "__main__":
    main()
