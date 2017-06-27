# The general approach to the Caesar Cipher problem:
# For each letter in our message, look up the index in the alphabet (represented by a string).
# Then, add 13 to that index.
# If the value is greater than or equal to 26, then subtract 26 (to start over at 'a').


encoded_message =  "lbh zhfg hayrnea jung lbh unir yrnearq"
# encoded_message = raw_input("enter the messge here: ")

# We will use a string that contains the alphabet.
# This lets us use the `in` operator to see if a character in our message is a letter.
# Also, we can ask for the `.index` of a letter.
alphabet = "abcdefghijklmnopqrstuvwxyz" 

rotate_by = 13 # We're doing ROT 13

# Create a variable with an empty string that we'll add decoded letters to.
decoded_message = ""

# Iterate through the characters in our message.
for letter in encoded_message:
    # Anything that's not in the alphabet, just pass through to the decoded_message.
    if letter not in alphabet:
        decoded_message = decoded_message + letter
    else:
        # Grab the index in the alphabet.
        index_in_alphabet = alphabet.index(letter)

        # Add 13 (or whatever the amount of rotation is.)
        new_index = index_in_alphabet + rotate_by

        # See if we've exceeded the length of the alphabet.
        if new_index >= len(alphabet):
            
            # Shift back to the beginning of the alphabet, if necessary.
            new_index = new_index - len(alphabet)
            
        # Add the rotated letter to decoded_message.
        decoded_message = decoded_message + alphabet[new_index]

print decoded_message
