# Add your constants here


# BASE_URL = "https://restful-booker.herokuapp.com"   #this is normal
# def base_url():
#  return "https://restful-booker.herokuapp.com"    #this is function constarint

class APIConstants(object):  # this is a class
    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # update,put,p[atch,delete -booking id

    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
