from opencage.geocoder import OpenCageGeocode

def get_coordinates(sity, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(sity, language='ru')
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"

    except Exception as e:
        return f"Возникла ошибка: {e}"

key = 'a10d03e8684b411783e3c1143a8ddaad'
city = "London"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
