import pickle

def main_menu(menu_text, max):
  choice = 0
  while choice not in range(1, max):
    print menu_text
    choice = int(raw_input("What do you want to do? "))
  return choice

# =======================================

def get_info(field):
  return raw_input("%s: " % field)

def get_name():
  return get_info("Name")

def get_number():
  return get_info("Phone Number")

def get_email():
  return get_info("Email")

def get_web():
  return get_info("Website")

# =======================================

def print_entry(name, book):
  if name in book:
    print "Found entry for %s: %s, %s [%s]" % (name, 
                                              book[name]['number'],
                                              book[name]['email'],
                                              book[name]['web'],
                                              )
  else:
    print "No one by that name"

def set_entry(book):
  name = get_name()
  number = get_number()
  email = get_email()
  web = get_web()
  book[name] = {
    "number": number,
    "email": email,
    "web": web,
  }
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

def save_entries(book):
  save_file = open('pickled-phonebook.dat', 'w')
  pickle.dump(book, save_file)
  save_file.close()
  print "saved!"

def load_entries():
  save_file = open('pickled-phonebook.dat', 'r')
  book = pickle.load(save_file)
  save_file.close()
  return book
  

# =======================================
def main():
  phonebook = {} # empty phonebook

  menu_choice = -1 # initial dummy value
  text_for_main_menu = """\n\n\nElectronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries to a file
6. Restore saved entries from file
7. Quit"""

  QUIT_OPTION = 7

  while menu_choice != QUIT_OPTION:
    # Get the choice from the user.
    menu_choice = main_menu(text_for_main_menu, QUIT_OPTION + 1)

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
    
    elif menu_choice == 5:
      # Show the whole phonebook.
      save_entries(phonebook)

    elif menu_choice == 6:
      # Show the whole phonebook.
      phonebook = load_entries()
  
  # All done.
  print "Bye"

main()