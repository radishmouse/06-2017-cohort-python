
total_bill = int(raw_input('Total bill amount? '))
level_of_service = raw_input('Level of service? ')

tip_text = 'Tip amount: %.2f'
tip = 0.0

total_text = 'Total amount: %.2f'

if level_of_service == 'good':
  tip = total_bill * 0.2
if level_of_service == 'fair':
  tip = total_bill * 0.15
if level_of_service == 'bad':
  tip = total_bill * 0.1

print tip_text % tip
print total_text % (total_bill + tip)
  