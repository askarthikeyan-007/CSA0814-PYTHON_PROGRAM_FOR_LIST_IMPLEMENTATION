import calendar
def weekdays_and_first_monday(year, month):
    weekdays = sum(1 for day in range(1, calendar.monthrange(year, month)[1] + 1) 
                   if calendar.weekday(year, month, day) < 5)
    first_monday = next(day for day in range(1, 8) 
                        if calendar.weekday(year, month, day) == 0)
    return weekdays, first_monday
year, month = 2023, 10
weekdays, first_monday = weekdays_and_first_monday(year, month)
print(f"Weekdays: {weekdays}, First Monday: {first_monday}")
