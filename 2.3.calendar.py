from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar


def main():
    # create plain text calendar
    # c = calendar.TextCalendar(calendar.MONDAY)
    # st = c.formatmonth(2017, 1, 0, 0)
    # print(st)

    # create html formatted calendar
    hc = calendar.HTMLCalendar(calendar.MONDAY)
    st = hc.formatmonth(2017, 1)
    print(st)

if __name__ == "__main__":
    main()
