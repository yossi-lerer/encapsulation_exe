# part 1
# step 1 - Private Username
class UserProfile:
    def __init__(self, username):
        self.__username = username
    @property
    def username(self):
        return self.__username
yossi = UserProfile("yossi")
print(yossi.username)
# print(yossi.__username)
# AttributeError: Python does not recognize this variable.
# step 2 - Private Email with Getter
class UserProfile:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
bob = UserProfile("bob", "bob@mail.com")
print(bob.username)
print(bob.email)
# step 3 - Username Setter with Validation
class UserProfile:
    def __init__(self, username):
        self.__username = username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        if len(username) >= 3:
            self.__username = username
        else:
            print("username too short")
yossi = UserProfile("yossi")
yossi.username = "yo"
print(yossi.__dict__)
yossi.username = "yosss"
print(yossi.__dict__)
