from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    # construct basic timedeltas and print it
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("Now: ", now)

    print("Using timedelta: ", str(now + timedelta(days=365)))

    # How many days until april fools day

    aprilFoolsDay = date(now.year, 4, 1)
    today = date.today()

    if aprilFoolsDay < today:
        print("April fools day already went by %d days ago" % ((today - aprilFoolsDay).days))
        aprilFoolsDay = aprilFoolsDay.replace(year=today.year + 1)

    timeToAprilFoolsDay = aprilFoolsDay - today
    print("It's just " + str(timeToAprilFoolsDay.days) + " days until April fools day")

if __name__ == "__main__":
    main()
