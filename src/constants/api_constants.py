#Add your constant here

class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update,put,p[atch,delete -booking id

    def url_patch_put_delete_booking(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)