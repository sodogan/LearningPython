import calendar


def main():
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2018, 12, 9, 0)
    print(st)

    # Create HTML calendar
    c = calendar.HTMLCalendar(calendar.SUNDAY)
    st = c.formatmonth(2018, 12)
    print(st)

    # Loop over the days of a month
    for i in c.itermonthdays(2017, 8):
        print("i is", i)

    for name in calendar.month_name:
        print(name)

    for day in calendar.day_name:
        print(day)

    for m in range(1, 13):
        cal = calendar.monthcalendar(2018, m)
        weekone = cal[0]
        weektwo = cal[1]
        # find first friday
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
        print("%10s %2d" % (calendar.month_name[m], meetday))


if __name__ == "__main__":
    main()
