import requests
import json
import csv

#DEFAULT VARIABLES
USERTECH_API_URL = "http://carvago-temporary.utdigit.com:8000/api/cars?limit=1000&offset="
DEFAULT_OFFSET = 0

#DOWNLOADING PROCESS
print("Starting downloading process...")

current_offset = DEFAULT_OFFSET

with open('data/out/tables/data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["pic", "ahoj"])

while 1 == 1:
    url = USERTECH_API_URL + str(current_offset)

    response = requests.get(url)
    response = json.loads(response.text)

    last = 0

    for ad in response:
        if ad == "error":
            last = 1
        break

    if last:
        break

    current_offset += 1000

print("Job done!")
