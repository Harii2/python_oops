class User:
    counter = 0

    def __init__(self, name):
        self.name = name
        type(self).counter += 1

    def get_counter(self):
        return User.counter


# from user import User
user_object = User("New User")
print(user_object.get_counter())
