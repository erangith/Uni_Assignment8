#########################
# Assignment 8
# Author: <Dadayakkara Dewege poorna Erangith Wijesire> 



import requests

def getApiData():
    with requests.get("https://data.novascotia.ca/resource/m862-kmjy.json?$limit=1000") as resp:
        tmp = resp.json()

    return tmp

api_data = getApiData()

municipalities = list(set([i['geography'] for i in api_data]))
municipalities.sort()

while True:

    for index, m in enumerate(municipalities, start=1):
        print(f"{index}. {m}")

    userInputs = int(input("Enter the index for the municipality: "))

    if userInputs - 1 > len(municipalities):
        print("Out of range")
        continue

    municipality = municipalities[userInputs - 1]

    year = input("Please enter a year: ")

    stats = [i for i in api_data if i.get('geography') == municipality and i.get('year') == year]

    print(f"Crime Statistics for {municipality}")

    for record in stats:
        print(f"{record.get('violations')} -> {record.get('incidents', '0')}")

    print("Total violations:", sum([int(i.get("incidents", 0)) for i in stats]))

    sel = ''
    while sel.lower() not in ("yes", 'no'):
        sel = input("Would you like to examine more entries? (yes/no): ")

        if sel not in ('yes', 'no'):
            print("Invalid response")

    if sel.lower() == "no":
        break