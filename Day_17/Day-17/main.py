# How to create a Class
"""# To Create a Class: Use (class ClassName:).Pascal case being used for the class name.
class User:
    pass
# Create User class.
user_1 = User()
# Create Object user_1 from the User class"""

# Working with Attributes, Class Constructors and the __init__() Function

"""class User:

    def __init__(self, user_id, user_name):
        # This function is normally used to initialize the attributes of Object
        self.id = user_id
        self.username = user_name
        self.followers = 0
        # add Attribute followers to the User class


user_1 = User("0001", "vuong")
# Create an Object user_1 with 2 Attribute user_id = "0001" and username = "Vuong"
print(user_1.followers)"""

# Adding Methods to a Class
# To add a methods to a Class, just need to create a function inside the class


class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """Increase followers for followed user and increase followers for following user"""
        user.followers += 1
        self.following += 1

user_1 = User("0001", "vuong")
user_2 = User("0002", "quynh")

user_1.follow(user_2)
# user_1 follow user_2

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)