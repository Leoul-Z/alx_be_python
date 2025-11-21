import datetime
from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(day):
    today = datetime.now()
    future_date = today + timedelta(days=day)
    print("Future date", future_date.strftime("%Y-%m-%d %H:%M:%S"))


display_current_datetime()
day = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(day)
