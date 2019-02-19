import requests
import json
import csv
from keboola import docker

#GET DATA FROM CONFIG JSON
cfg = docker.Config('/data/')
params = cfg.get_parameters()

#DOWNLOADING PROCESS
print("Starting downloading process...")

current_offset = params['DEFAULT_OFFSET']

with open('/data/out/tables/data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)

    writer.writerow([
        "power_hp",
        "cubic_capacity",
        "power",
        "number_of_seats",
        "features",
        "fuel_type",
        "transmission",
        "vehicle_type",
        "fuel_consumption_urban",
        "fuel_consumption_extra_urban",
        "fuel_consumption_combined",
        "fuel_consumption_unit",
        "power_unit",
        "weight",
        "number_of_gears",
        "carbon_dioxide_emission",
        "drive",
        "car_style",
        "emission_class",
        "equipment_version",
        "manufactured_from",
        "manufactured_to",
        "interior_material",
        "number_of_airbags",
        "air_conditioning",
        "audio",
        "auxiliary_heating",
        "ceiling_material",
        "cruise_control",
        "display",
        "door_count",
        "folding_roof",
        "hands_free",
        "headlights_type",
        "parking_camera",
        "parking_sensors",
        "rear_spoiler",
        "sliding_doors",
        "spare_tyre",
        "sunroof",
        "tailgate_opening",
        "trailer_coupling",
        "id",
        "title",
        "model_edition"
    ])

    while 1 == 1:
        print("Downloading for offset: " + str(current_offset))

        url = params['URL'] + "?" + params['LIMIT_PARAM'] + "=" + params['LIMIT'] + "&" + params['OFFSET_PARAM'] + "=" + str(current_offset)

        response = requests.get(url)
        response = json.loads(response.text)

        last = 0

        for ad in response:
            if ad == "error":
                last = 1
            break

        if last:
            break

        for row in response:
            try:
                writer.writerow([
                    row["power_hp"],
                    row["cubic_capacity"],
                    row["power"],
                    row["number_of_seats"],
                    row["features"],
                    row["fuel_type"],
                    row["transmission"],
                    row["vehicle_type"],
                    row["fuel_consumption_urban"],
                    row["fuel_consumption_extra_urban"],
                    row["fuel_consumption_combined"],
                    row["fuel_consumption_unit"],
                    row["power_unit"],
                    row["weight"],
                    row["number_of_gears"],
                    row["carbon_dioxide_emission"],
                    row["drive"],
                    row["car_style"],
                    row["emission_class"],
                    row["equipment_version"],
                    row["manufactured_from"],
                    row["manufactured_to"],
                    row["interior_material"],
                    row["number_of_airbags"],
                    row["air_conditioning"],
                    row["audio"],
                    row["auxiliary_heating"],
                    row["ceiling_material"],
                    row["cruise_control"],
                    row["display"],
                    row["door_count"],
                    row["folding_roof"],
                    row["hands_free"],
                    row["headlights_type"],
                    row["parking_camera"],
                    row["parking_sensors"],
                    row["rear_spoiler"],
                    row["sliding_doors"],
                    row["spare_tyre"],
                    row["sunroof"],
                    row["tailgate_opening"],
                    row["trailer_coupling"],
                    row["id"],
                    row["title"],
                    row["model_edition"]
                ])
            except:
                print("Writing error")

        current_offset += params['OFFSET']

print("Job done!")
