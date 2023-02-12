from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = str(request.POST['city'])
        encoded_city = urllib.request.quote(city)
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+encoded_city+'&appid=aed2b65f33185f4762715a0d72ea940f').read()
        json_data = json.loads(res)
        temps = str("{:.2f}".format(float(json_data['main']['temp']) - 273.15)) + " C" + chr(176) + " | " + str("{:.2f}".format((float(json_data['main']['temp']) - 273.15)*1.8 + 32)) + " F" + chr(176)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ', ' +
            str(json_data['coord']['lat']),
            "temp": temps,
            "pressure": str(json_data['main']['pressure']) + " hPa",
            "humidity": str(json_data['main']['humidity']) + "%",
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': str(city[0].upper() + city[1:]), 'data': data})
