import time
import requests
import json
# make a get request to the api
response = requests.get("https://api.weather.gov/alerts")
print(response.status_code)
# save the response content into out_%Y%m%d-%H%M%S.json to examine the text
timestr = time.strftime("%Y%m%d-%H%M%S")
file = open("out_" + timestr + ".json", "wb")
file.write(response.content)
file.close()

# append the filename to data_list
file = open("data_list.txt", "a")
file.write("out_" + timestr + ".json" + "\n")
file.close()

