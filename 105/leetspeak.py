text = "hello world"
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [ 4,   3,   6,   1,   0,   5,   7]

translation = ""

uppercased_text = text.upper()
for letter in uppercased_text:
  print "the letter is ", letter
  # print "the index is ", letters_to_convert.index(letter)
  counter = 0
  letter_to_add_to_translation = ""
  for letter_to_convert in letters_to_convert:
    # print "looking at ", letter_to_convert
    if letter == letter_to_convert:
      print "\n********** found it! %s \n\n" % letter
      print "want to replace with %s" % numbers[counter]
      # translation = translation + str(numbers[counter])
      letter_to_add_to_translation = str(numbers[counter])
      break # dear self, break out of loop after finding good replacement
      # otherwise, you overwrite with the original letter
    else:
      print "just use", letter 
      # translation = translation + letter
      letter_to_add_to_translation = letter
    
    counter = counter + 1
  translation = translation + letter_to_add_to_translation
  print translation
