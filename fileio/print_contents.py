
def prompt_for_file():
  return raw_input("Please enter file name: ")

def get_contents(filename):
  the_file = open(filename)
  contents = the_file.read()
  the_file.close()
  return contents

def main():
  fname = prompt_for_file()
  print get_contents(fname)

main()