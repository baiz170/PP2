from datetime import datetime, timedelta

current_date = datetime.today()
date_minus_five = current_date - timedelta(days=5)


yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)


current_time_no_microseconds = datetime.now().replace(microsecond=0)


date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 10, 15, 30, 0)
difference_in_seconds = abs((date2 - date1).total_seconds())


print("Current date:", current_date.strftime('%Y-%m-%d'))
print("Date 5 days ago:", date_minus_five.strftime('%Y-%m-%d'))
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", current_date.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))
print("Current time without microseconds:", current_time_no_microseconds)
print("Difference between two dates in seconds:", difference_in_seconds)
