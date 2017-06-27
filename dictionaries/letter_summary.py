
def letter_histogram(word):
  histogram = {}
  for l in word:
    if l in histogram:
      histogram[l] = histogram[l] + 1
    else:
      histogram[l] = 1
  return histogram

print letter_histogram('banana')

def top_3(histogram):
  top_values = histogram.values()[:3]
  total_printed = 0
  for i in top_values:
    for k, v in histogram.items():
      if v == i and total_printed < 3:
        print "%s: %d" % (k, v)
        total_printed = total_printed + 1

print top_3(letter_histogram('bananaboat'))