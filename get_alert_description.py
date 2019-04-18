import json

filename = "data_list.txt"
data_list = open(filename).read().splitlines()

alert_msg = ""
file = open("alert_description.txt", "w")

for item in data_list:
    with open(item) as json_file:
        json_data = json.load(json_file)
        #extract the features(alert) list from json_data
        features = json_data.get('features')
        for pieces in features:
            alert           = "Alert:\n" + pieces.get('properties').get('description') + "\n"
            instruction     = "Instruction:\n" + pieces.get('properties').get('instruction') + "\n" 
            alert_msg = alert_msg + alert + instruction

file.write(alert_msg)
file.close()

