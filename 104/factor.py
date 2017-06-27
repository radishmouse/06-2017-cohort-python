
go = True
while go:
  factors = []
  number = int(raw_input("Enter a number to factor: "))
  if number < 100000:
    for i in xrange(1, number):
      if (number % i == 0):
        factors.append(i)
    print factors
  else:
    print "Too big."
  answer = raw_input("another (Y/N)? ")
  if answer.upper() != "Y":
    go = False
print "k. thanks. bye!"
