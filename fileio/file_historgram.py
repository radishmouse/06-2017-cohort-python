
def letter_histogram(word):
  histogram = {}
  for l in word:
    if l in histogram:
      histogram[l] = histogram[l] + 1
    else:
      histogram[l] = 1
  return histogram

def word_histogram(paragraph):
  histogram = {}
  word_list = paragraph.split()
  for word in word_list:
    if word in histogram:
      histogram[word] = histogram[word] + 1
    else:
      histogram[word] = 1
  return histogram

def prompt_for_file():
  return raw_input("Please enter file name: ")

def get_contents(filename):
  the_file = open(filename)
  contents = the_file.read()
  the_file.close()
  return contents

def main():
  fname = prompt_for_file()
  contents = get_contents(fname)
  print "letter histogram: "
  print letter_histogram(contents)
  print "\n\n\nword histogram: "
  print word_histogram(contents)

main()