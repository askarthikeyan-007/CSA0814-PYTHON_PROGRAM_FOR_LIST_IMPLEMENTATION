from datetime import datetime as dt
d1 = dt.strptime(input("Enter first date (YYYY-MM-DD): "), "%Y-%m-%d")
d2 = dt.strptime(input("Enter second date (YYYY-MM-DD): "), "%Y-%m-%d")
diff = d2 - d1
years = diff.days // 365
months = (diff.days % 365) // 30
days = (diff.days % 365) % 302005
print(f"Years: {years}, Months: {months}, Days: {days}")
