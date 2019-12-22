from raid import Raid
import csv


def clean_name(str):
    name = str[2:]
    name = name[:-2]

    return name

file = open('../dump.csv')
fileReader = csv.reader(file)
data = list(fileReader)

raids = []

for row in range(len(data)):
    for x in data[row]:
        if x == "-- start --":

            event_name = data[row+2][0]
            event_date = data[row+2][1]
            event_time = data[row+2][2]
            event_description = data[row+2][3]

            # Create a new raid
            raid_obj = Raid(event_name, event_date, event_time, event_description)
            raids.append(raid_obj)

            #Iterate through all roles
            i = 3

            while i < 14:
                for num_tank in range(len(data[row+i])):
                    if num_tank == 0:
                        role = str(data[row+i][num_tank])
                        continue

                    temp_str = str(data[row+i][num_tank]).split("--")

                    if len(temp_str) > 1:
                        raid_obj.add_attendee(role, clean_name(temp_str[2]))

                i += 1

print(len(raids))
