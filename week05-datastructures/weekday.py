# Importing datetime module
import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

today_day = datetime.datetime.now().strftime("%A")

if today_day in weekdays:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
