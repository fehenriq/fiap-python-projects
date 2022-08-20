from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")
location = geolocator.geocode("IASD Central de Suzano")
print(location.address)
print((location.latitude, location.longitude))
