class Person(object):
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0
    self.unique_greetings = {}
  
  def greet(self, other_person):
    self.greeting_count = self.greeting_count + 1
    if other_person.name not in self.unique_greetings:
      self.unique_greetings[other_person.name] = 0
    self.unique_greetings[other_person.name] = self.unique_greetings[other_person.name] + 1
    print 'Hello %s, I am %s' % (other_person.name, self.name)

  def print_contact_info(self):
    print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

  def add_friend(self, friend):
    self.friends.append(friend)
  
  def num_friends(self):
    return len(self.friends)
  
  def num_unique_people_greeted(self):
    return len(self.unique_greetings.keys())
  
  def __repr__(self):
    return '%s %s %s' % (self.name, self.email, self.phone)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
luke = Person('Luke', 'luke@skywalker.com', '123-789-3456')
darth = Person('Darth', 'darth@vader.com', '123-666-3456')

sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(darth)
jordan.greet(luke)
sonny.greet(luke)

print sonny.greeting_count
print jordan.greeting_count

print "%s - %s" % (sonny.email, sonny.phone)
print "%s - %s" % (jordan.email, jordan.phone)

sonny.print_contact_info()
jordan.print_contact_info()

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
jordan.add_friend(sonny)
sonny.add_friend(jordan)

print jordan.num_friends()
print sonny.num_friends()

print jordan
print sonny

print jordan.num_unique_people_greeted()
print sonny.num_unique_people_greeted()