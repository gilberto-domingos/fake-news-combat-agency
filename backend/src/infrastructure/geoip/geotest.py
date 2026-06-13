import geoip2.database

reader = geoip2.database.Reader(
    # "src/infrastructure/geoip/GeoLite2-City.mmdb"
    "GeoLite2-City.mmdb"
)

response = reader.city("200.160.2.3")

print(response.city.name)
print(response.subdivisions.most_specific.name)
print(response.country.name)
