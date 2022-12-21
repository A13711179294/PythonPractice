before_hours, before_minutes, after_hours, after_minutes = map(int, input().split())
hour_gap = after_hours - before_hours - 1
minute_gap = after_minutes + 60 - before_minutes
if minute_gap >= 60:
    print(hour_gap + 1, minute_gap-60)
else:
    print(hour_gap, minute_gap)
