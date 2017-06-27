
def main_menu():
  choice = 0
  while choice not in range(1, 6):
    print """\n\n\nElectronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit"""
    choice = int(raw_input("What do you want to do (1-5)? "))
  return choice

# =======================================

def get_name():
  return raw_input("Name: ")

def get_number():
  return raw_input("Phone Number: ")

# =======================================

def print_entry(name, book):
  if name in book:
    print "Found entry for %s: %s" % (name, book[name])
  else:
    print "No one by that name"

def set_entry(book):
  name = get_name()
  number = get_number()
  book[name] = number
  print "Entry stored for %s." % name
  return book

def delete_entry(book):
  name = get_name()
  if name in book:
    del book[name]
    print "Deleted entry for %s" % name
  return book

def print_phonebook(book):
  for k in book.keys():
    print_entry(k, book)

# =======================================

def main():
  phonebook = {} # empty phonebook

  menu_choice = -1 # initial dummy value

  while menu_choice != 5:
    # Get the choice from the user.
    menu_choice = main_menu()

    if menu_choice == 1:
      # They want to add.
      # Prompt for name, print the entry.
      name = get_name()
      print_entry(name, phonebook)
    
    elif menu_choice == 2:
      # They want to set a phone number.
      phonebook = set_entry(phonebook)

    elif menu_choice == 3:
      # They want to delete an entry.
      phonebook = delete_entry(phonebook)
    
    elif menu_choice == 4:
      # Show the whole phonebook.
      print_phonebook(phonebook)
  
  # All done.
  print "Bye"

main()