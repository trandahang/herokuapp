class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):  #in object
        return "username is '%s', password is '%s'" % (self.username, self.password)