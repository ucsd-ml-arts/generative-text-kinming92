import json

filename = "data_list.txt"
data_list = open(filename).read().splitlines()

alert_report = ""
file = open("out.txt", "w")

for item in data_list:
    with open(item) as json_file:
        json_data = json.load(json_file)
        #extract the features(alert) list from json_data
        features = json_data.get('features')
        for pieces in features:
            if pieces.get('properties').get('headline') is None:
                headline = ""
            else:
                headline = pieces.get('properties').get('headline') + "\n"
            sent            = "Sent           :\t" + pieces.get('properties').get('sent') + "\n"
            effective       = "Effective      :\t" + pieces.get('properties').get('effective') + "\n"
            status          = "Status         :\t" + pieces.get('properties').get('status') + "\n" 
            severity        = "Severity       :\t" + pieces.get('properties').get('severity') + "\n"
            urgency         = "Urgency        :\t" + pieces.get('properties').get('urgency') + "\n"
            event           = "Event          :\t" + pieces.get('properties').get('event') + "\n"
            alert           = "Alert:\n" 
            description     = pieces.get('properties').get('description') + "\n"
            instruction     = "Instruction:\n" + pieces.get('properties').get('instruction') + "\n" 
            forecast_office = "Forecast Office:\t" + pieces.get('properties').get('senderName') + "\n"
            alert_report = alert_report + sent + effective + status + severity + urgency + forecast_office + event + alert + headline + description + instruction 
                    
# print (alert_report)
file.write(alert_report)
file.close()
