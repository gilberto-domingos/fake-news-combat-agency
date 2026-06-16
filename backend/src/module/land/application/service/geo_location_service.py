from src.module.land.domain.repository_int.geo_location_int import GeoLocationServiceInt
from src.module.land.infrastructure.geoip.geoip_reader import GeoIPReader


class GeoLocationService(GeoLocationServiceInt):

    def __init__(self, reader: GeoIPReader):
        self.reader = reader

    def get_city(self, ip: str) -> str | None:
        return self.reader.get_city(ip)

    def get_country(self, ip: str) -> str | None:
        return self.reader.get_country(ip)
