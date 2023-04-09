import datetime
from dateutil.relativedelta import relativedelta

class Date:
    """A date in YYYY-MM-DD format"""
    def __init__(self, date):
        print("Date object created using value: {}".format(date))
        self.year, self.month, self.day = date.split("-")

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def __sub__(self, other):
        date1 = datetime.date(int(self.year), int(self.month), int(self.day))
        date2 = datetime.date(int(other.year), int(other.month), int(other.day))
        """We return the date difference as a full date"""
        """That means, 1-JANUARY-2023 minus month(1) is 1-DECEMBER-2022"""
        """We must also return it as a Date object"""
        return Date(str(date1 - relativedelta(months=1)))

def current_date():
    """Return the current date in YYYY-MM-DD format"""
    return Date(datetime.date.today().strftime("%Y-%m-%d"))

def month(n):
    """Return a date n months ago"""
    return Date((datetime.date.today() - relativedelta(months=n)).strftime("%Y-%m-%d"))
