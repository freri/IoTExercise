import json
if __name__ == "__main__":

    personal_data = {
        "projectName": "",
        "company": "",
        "deviceList": [ 
            {
                "deviceID": "",
                "deviceName": "",
                "deviceType": ""
            }
        ]}

    for key in personal_data.keys():
        if key == "deviceList":
            for item in personal_data[key]:
                for key in item:
                    item[key] = input('Enter ' + key + ":")
        else:
            personal_data[key] = input('Enter '+ key + ":")

    json.dump(personal_data,open("personal_data.json","w"))
    personalData = json.load(open("personal_data.json"))
    print(personalData)