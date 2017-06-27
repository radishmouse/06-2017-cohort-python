prompt_text = ('What is your name? ')
name = raw_input(prompt_text)
greeting = 'Hello, %s!' % name
print greeting.upper()
print 'YOUR NAME HAS %d LETTERS IN IT! AWESOME!' % len(name)
