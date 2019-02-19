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
        "model_edition",
        "model_family",
        "make"
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
                    try:
                        features.append(feature['const_key'])
                    except:
                        continue

                fuel_type = "null"

                try:
                    fuel_type = row["fuel_type"]["const_key"]
                except:
                    fuel_type = row["fuel_type"]

                transmission = "null"

                try:
                    transmission = row["transmission"]["const_key"]
                except:
                    transmission = row["transmission"]

                vehicle_type = "null"

                try:
                    vehicle_type = row["vehicle_type"]["const_key"]
                except:
                    vehicle_type = row["vehicle_type"]

                car_style = "null"

                try:
                    car_style = row["car_style"]["const_key"]
                except:
                    car_style = row["car_style"]

                emission_class = "null"

                try:
                    emission_class = row["emission_class"]["const_key"]
                except:
                    emission_class = row["emission_class"]

                interior_material = "null"

                try:
                    interior_material = row["interior_material"]["const_key"]
                except:
                    interior_material = row["interior_material"]

                number_of_airbags = "null"

                try:
                    number_of_airbags = row["number_of_airbags"]["const_key"]
                except:
                    number_of_airbags = row["number_of_airbags"]

                air_conditioning = "null"

                try:
                    air_conditioning = row["air_conditioning"]["const_key"]
                except:
                    air_conditioning = row["air_conditioning"]

                audio = "null"

                try:
                    audio = row["audio"]["const_key"]
                except:
                    audio = row["audio"]

                auxiliary_heating = "null"

                try:
                    auxiliary_heating = row["auxiliary_heating"]["const_key"]
                except:
                    auxiliary_heating = row["auxiliary_heating"]

                ceiling_material = "null"

                try:
                    ceiling_material = row["ceiling_material"]["const_key"]
                except:
                    ceiling_material = row["ceiling_material"]

                cruise_control = "null"

                try:
                    cruise_control = row["cruise_control"]["const_key"]
                except:
                    cruise_control = row["cruise_control"]

                display = "null"

                try:
                    display = row["display"]["const_key"]
                except:
                    display = row["display"]

                door_count = "null"

                try:
                    door_count = row["door_count"]["const_key"]
                except:
                    door_count = row["door_count"]

                folding_roof = "null"

                try:
                    folding_roof = row["folding_roof"]["const_key"]
                except:
                    folding_roof = row["folding_roof"]

                hands_free = "null"

                try:
                    hands_free = row["hands_free"]["const_key"]
                except:
                    hands_free = row["hands_free"]

                headlights_type = "null"

                try:
                    headlights_type = row["headlights_type"]["const_key"]
                except:
                    headlights_type = row["headlights_type"]

                parking_camera = "null"

                try:
                    parking_camera = row["parking_camera"]["const_key"]
                except:
                    parking_camera = row["parking_camera"]

                parking_sensors = "null"

                try:
                    parking_sensors = row["parking_sensors"]["const_key"]
                except:
                    parking_sensors = row["parking_sensors"]

                rear_spoiler = "null"

                try:
                    rear_spoiler = row["rear_spoiler"]["const_key"]
                except:
                    rear_spoiler = row["rear_spoiler"]

                sliding_doors = "null"

                try:
                    sliding_doors = row["sliding_doors"]["const_key"]
                except:
                    sliding_doors = row["sliding_doors"]

                spare_tyre = "null"

                try:
                    spare_tyre = row["spare_tyre"]["const_key"]
                except:
                    spare_tyre = row["spare_tyre"]

                sunroof = "null"

                try:
                    sunroof = row["sunroof"]["const_key"]
                except:
                    sunroof = row["sunroof"]

                tailgate_opening = "null"

                try:
                    tailgate_opening = row["tailgate_opening"]["const_key"]
                except:
                    tailgate_opening = row["tailgate_opening"]

                trailer_coupling = "null"

                try:
                    trailer_coupling = row["trailer_coupling"]["const_key"]
                except:
                    trailer_coupling = row["trailer_coupling"]

                model_edition = "null"
                model_family = "null"
                make_model = "null"

                try:
                    model_edition = row["model_edition"]["const_key"],
                    model_family = row["model_edition"]["model_family"]["const_key"],
                    make_model = row["model_edition"]["model_family"]["make"]["const_key"]
                except:
                    model_edition = row["model_edition"]
                    model_family = row["model_edition"]
                    make_model = row["model_edition"]

                writer.writerow([
                    row["power_hp"],
                    row["cubic_capacity"],
                    row["power"],
                    row["number_of_seats"],
                    features,
                    fuel_type,
                    transmission,
                    vehicle_type,
                    row["fuel_consumption_urban"],
                    row["fuel_consumption_extra_urban"],
                    row["fuel_consumption_combined"],
                    row["fuel_consumption_unit"],
                    row["power_unit"],
                    row["weight"],
                    row["number_of_gears"],
                    row["carbon_dioxide_emission"],
                    row["drive"],
                    car_style,
                    emission_class,
                    row["equipment_version"],
                    row["manufactured_from"],
                    row["manufactured_to"],
                    interior_material,
                    number_of_airbags,
                    air_conditioning,
                    audio,
                    auxiliary_heating,
                    ceiling_material,
                    cruise_control,
                    display,
                    door_count,
                    folding_roof,
                    hands_free,
                    headlights_type,
                    parking_camera,
                    parking_sensors,
                    rear_spoiler,
                    sliding_doors,
                    spare_tyre,
                    sunroof,
                    tailgate_opening,
                    trailer_coupling,
                    row["id"],
                    row["title"],
                    model_edition,
                    model_family,
                    make_model
                ])
            except Exception as e:
                print(e)

        current_offset += int(params['OFFSET'])

print("Job done!")
