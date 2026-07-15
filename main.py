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
# step 4 - Private Follower Count
class UserProfile:
    def __init__(self, username):
        self.username = username
        self.__followers = 0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers += 1
    def unfollow(self):
        self.__followers -= 1
yossi = UserProfile("yossi")
yossi.follow()
yossi.follow()
yossi.follow()
yossi.unfollow()
print(yossi.followers)
# step 5 - Protected Bio Field
class UserProfile:
    def __init__(self, username, bio):
        self.username = username
        self._bio = bio
    @property
    def bio(self):
        return self._bio
class VerifiedUser(UserProfile):
    def __init__(self, username, bio, badge):
        super().__init__(username, bio)
        self.badge = badge
    def full_description(self):
        print(f"{self.username} [{self.badge}]: {self._bio}")
celeb = VerifiedUser("celeb", "Singer and songwriter", "✓")
celeb.full_description()
# step 6 - Age Setter with Range Check
class UserProfile:
    def __init__(self, username, age):
        self.username = username
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if 13 <= age <= 120:
            self.__age = age
        else:
            print("Invalid age.")
dan = UserProfile("dan", 18)
print(dan.__dict__)
dan.age = 10
dan.age = 200
dan.age = 25
print(dan.__dict__)
# step 7 - Password Protection
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    def check_password(self, attempt):
        return True if attempt == self.__password else False
    def change_password(self, old, new):
        if self.__password == old:
            self.__password = new
        else:
            print("Incorrect old password.")
admin = UserAccount("admin", "secret")
print(admin.check_password("wrong"))
admin.change_password("secre", "new123")