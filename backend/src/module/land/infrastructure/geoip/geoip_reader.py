import geoip2.database


class GeoIPReader:

    def __init__(self, db_path: str):
        self.reader = geoip2.database.Reader(db_path)

    def get_city(self, ip: str) -> str | None:
        try:
            # response = self.reader.city("200.160.2.3")
            response = self.reader.city(ip)
            city = response.city.name
            return city

        except Exception:
            return None

    def get_country(self, ip: str) -> str | None:
        try:
            response = self.reader.city(ip)
            return response.country.name
        except Exception:
            return None
