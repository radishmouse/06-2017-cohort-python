day = int(raw_input('Day (0-6)? '))

day_name = ''

if day == 0:
  day_name = 'Sunday'
if day == 1:
  day_name = 'Monday'
if day == 2:
  day_name = 'Tuesday'
if day == 3:
  day_name = 'Wednesday'
if day == 4:
  day_name = 'Thursday'
if day == 5:
  day_name = 'Friday'
if day == 6:
  day_name = 'Saturday'

print day_name