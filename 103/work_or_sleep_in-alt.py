day = int(raw_input('Day (0-6)? '))

sleep = False 

if day == 0:
  sleep = True
if day == 6:
  sleep = True

if sleep:
  print 'Sleep in'
else:
  print 'Go to work'