from datetime import date
from datetime import time
from datetime import datetime
# Represents time span. Used for time mathematics
from datetime import timedelta


def main():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("Now:", now)
    print("One year from now it will be:", str(now + timedelta(days=365)))
    print("In 2 days and 3 weeks, it will be:", str(now + timedelta(days=2, weeks=3)))

    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was", s)

    ### How many days until April Fool's Day?
    today = date.today()
    afd = date(today.year, 4, 1)
    if (afd < today):
        # April Fool's Day has already passedin this year
        print("April Fool's Day has already went by %d days ago" % (today - afd).days)
        afd = afd.replace(year=today.year + 1)
    time_to_afd = afd - today
    print("It's just {} days until April Fool's Day".format(time_to_afd.days))


if __name__ == "__main__":
    main()
