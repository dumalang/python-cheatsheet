from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Get today date
    today = date.today()
    print("Today's date is", today)

    # Print out date individual components
    print("Date components: ", today.month, today.day, today.year)

    # Print today weekday
    print("Today weekday is", today.weekday())
    days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
    print("Today weekday is", days[today.weekday()])

    # datetime object
    print("Datetime:", datetime.now())

    # get current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()
