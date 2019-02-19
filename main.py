import requests
import json
import csv
from keboola import docker

#GET DATA FROM CONFIG JSON
cfg = docker.Config('/data/')
params = cfg.get_parameters()

#DOWNLOADING PROCESS
print("Starting downloading process...")

current_offset = int(params['DEFAULT_OFFSET'])

with open(params['OUTPUT'], 'w') as csvfile:
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
                features = []

                for feature in row["features"]:
                    features.append(feature['const_key'])

                writer.writerow([
                    row["power_hp"],
                    row["cubic_capacity"],
                    row["power"],
                    row["number_of_seats"],
                    features,
                    row["fuel_type"]["const_key"],
                    row["transmission"]["const_key"],
                    row["vehicle_type"]["const_key"],
                    row["fuel_consumption_urban"],
                    row["fuel_consumption_extra_urban"],
                    row["fuel_consumption_combined"],
                    row["fuel_consumption_unit"],
                    row["power_unit"],
                    row["weight"],
                    row["number_of_gears"],
                    row["carbon_dioxide_emission"],
                    row["drive"],
                    row["car_style"]["const_key"],
                    row["emission_class"]["const_key"],
                    row["equipment_version"],
                    row["manufactured_from"],
                    row["manufactured_to"],
                    row["interior_material"]["const_key"],
                    row["number_of_airbags"]["const_key"],
                    row["air_conditioning"]["const_key"],
                    row["audio"]["const_key"],
                    row["auxiliary_heating"]["const_key"],
                    row["ceiling_material"]["const_key"],
                    row["cruise_control"]["const_key"],
                    row["display"]["const_key"],
                    row["door_count"]["const_key"],
                    row["folding_roof"]["const_key"],
                    row["hands_free"]["const_key"],
                    row["headlights_type"]["const_key"],
                    row["parking_camera"]["const_key"],
                    row["parking_sensors"]["const_key"],
                    row["rear_spoiler"]["const_key"],
                    row["sliding_doors"]["const_key"],
                    row["spare_tyre"]["const_key"],
                    row["sunroof"]["const_key"],
                    row["tailgate_opening"]["const_key"],
                    row["trailer_coupling"]["const_key"],
                    row["id"],
                    row["title"],
                    row["model_edition"]
                ])
            except:
                print("Writing error")

        current_offset += int(params['OFFSET'])

print("Job done!")
