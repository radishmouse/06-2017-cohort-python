
def set_contents(filename, text):
  the_file = open(filename, 'w')
  the_file.write(text)
  the_file.close()

def main():
  fname = raw_input("Please enter file name: ")
  contents = raw_input("Enter some text! ")
  set_contents(fname, contents)
  print "all done!"

main()