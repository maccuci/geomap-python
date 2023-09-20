import time


class GeoUtils:
    def __init__(self, app):
        self.app = app

    def get_address_by_location(self, latitude, longitude):
        coord = f"{latitude}, {longitude}"
        time.sleep(0.5)
        try:
            return self.app.reverse(coord).raw
        except:
            return self.get_address_by_location(latitude, longitude)
        pass

    def get_location_by_address(self, address):
        time.sleep(0.5)
        try:
            return self.app.geocode(address).raw
        except:
            return self.get_location_by_address(address)
        pass
