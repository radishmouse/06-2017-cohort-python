
def word_histogram(paragraph):
  histogram = {}
  word_list = paragraph.split()
  for word in word_list:
    if word in histogram:
      histogram[word] = histogram[word] + 1
    else:
      histogram[word] = 1
  return histogram

print word_histogram('to be or not to be')