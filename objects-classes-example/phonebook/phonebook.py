class Phonebook(object):
  def __init__(self):
    self.phonebook = {}
  
  def add_contact(self, contact):
    self.phonebook[contact.email] = contact

  def delete_contact(self, email):
    del self.phonebook[email]
  
  def show_all_entries(self):
    for c in self.phonebook:
      print c.show()
  
  def show_entry(self, email):
    print self.phonebook[email]

  def search(self, key_name, search_text):
    results = []

    # do some work
    for c in self.phonebook:
      if c[key_name] == search_text:
        results.append(c)

    return results

  