text = raw_input('Text? ')
stars = ''

# The width of the top and bottom rows of the banner
# is the length of the text + 2 stars + 2 spaces
for i in range(len(text) + 4):
  stars = stars + '*'

print stars
print "* %s *" % text
print stars