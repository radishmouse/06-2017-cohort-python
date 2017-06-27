class Contact(object):
    def __init__(self, first_name, last_name, email, phone):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.phone = phone
        
    def show(self):
        return "%s, %s - %s (%s)" % (self.last, self.first, self.email, self.phone)
