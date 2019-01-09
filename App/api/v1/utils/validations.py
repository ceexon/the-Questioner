
class UserValidation:
    '''' This class validates all user data to be filled in during login and signup '''

    def __init__(self, user_data):
        self.data = user_data

    # def check_all_fields(self):
    #     try:
    #         if not self.data["firstName"]:
    #             return "firstname is required"
