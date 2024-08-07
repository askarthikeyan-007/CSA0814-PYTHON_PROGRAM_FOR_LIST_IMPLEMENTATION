from datetime import datetime, timedelta
today = datetime.now()
first_day_of_next_month = datetime(today.year + (today.month // 12), ((today.month % 12) + 1), 1)
days_until_monday = (7 - first_day_of_next_month.weekday()) % 7
first_monday_of_next_month = first_day_of_next_month + timedelta(days=days_until_monday)
print(first_monday_of_next_month)
