from opencage.geocoder import OpenCageGeocode

key = 'a10d03e8684b411783e3c1143a8ddaad'
city = "Moscow"

def get_coordinates(sity, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"



key = 'a10d03e8684b411783e3c1143a8ddaad'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(f"Координаты города {sity}: {coordinates}")
