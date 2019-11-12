import requests
import json
import time

# the address we will make the request to
# TODO:  REPLACE WITH YOUR URL
url='https://test.herokuapp.com/'
dataUrl='https://test.herokuapp.com/api/data'
settingsUrl='https://test.herokuapp.com/api/settings'
statsUrl='https://test.herokuapp.com/api/statistics'

# make a get request to retrieve the current settings and stats, and extract the JSON from it
Settings = requests.get(settingUrl)
Stats = requests.get(statsUrl)

settings = Settings.json()
oldStats = Stats.json()

# get the color to the lightColor field of the settings object
colorStr = settings['lightColor']
# colorStr contains the color of the light selected on the webapp
# TODO: set the color of the led based on the color from the webapp


# initialize an empty dictionary
# TODO: fill up packet dictionary with the appropriate data
#			i.e. temperature, humidity, brightness data
packet = {}

# just a debug, comment it out when you know the script works
print(packet)

# submit the post request.
r = requests.post(dataUrl,json=packet)


# newStats dictionary, updated with the oldStats and the current reading
# TODO: update stats after reading new values from the sensors
newStats = {
  'avgTemperature': ,
  'avgHumidity': ,
  'avgBrightness': ,
  'timeInHot': ,
  'timeInCold': ,
  'timeInHumid': ,
  'timeInDry': ,
  'timeOn': ,
  'timeTotal': 
}

print(json.dumps(newStats))
r = requests.put(statsUrl, newStats)
print(r)
