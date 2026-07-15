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