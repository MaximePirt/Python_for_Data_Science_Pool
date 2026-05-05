import datetime as dt

january = dt.datetime(
	year=1970,
	month=1,
	day=1
)

now = dt.datetime.today()

delta = dt.timedelta()
delta =  now - january

seconds = delta.total_seconds()

print("Seconds since January 1, 1970:", f"{seconds:,.4f}", "or", "%.2e"%seconds, "in scientific notation")
print('{0:%b} {0:%d} {0:%Y}'.format(now, "day", "month", "year"))
