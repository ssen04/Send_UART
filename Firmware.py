import csv
import re

list_of_commands = []
cmd = ''


file = open("Firmware.csv")
csvreader = csv.reader(file)
header = next(csvreader)
# print(header)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows)
file.close()

# Change to command
# Rows
cmd_array = rows[0]
# Mode
mode = str(cmd_array[0])
# Ramp Rate
ramp_rate = str(cmd_array[1])
# Dwell Time
dwell_time = str(cmd_array[2])
# Load
load = str(cmd_array[3])
# Displacement
displacement = str(cmd_array[4])
# Spring Constant
spring_constant = str(cmd_array[5])
# Command
cmd_string = "$" + mode.lower() + "@" + ramp_rate + " " + dwell_time + " " + load + " " + displacement + " " + spring_constant + ":" + "1139\r"
print(cmd_string)



if (cmd_string == "" or cmd_string[0] != "$"):
    print("Invalid!")
else:
    for char in cmd_string:
        willContinue = True if (char != '\r') else False
        if willContinue and char != "$":
            cmd += char

    print(cmd)
    # Validate
    try:
        partitioned_cmd = re.split(':', cmd)
        print(partitioned_cmd)
        list_of_commands.append(partitioned_cmd[0])
        print(list_of_commands)
    except:
        print("Invalid!")

        
#
# # Verify from
# # $ to verify
# verify_dollar = cmd_string[0]
# partitioned_string = re.split(' |@|:', cmd_string)
# print(partitioned_string)
# # Get mode
# get_mode = partitioned_string[0][1:]
# print(get_mode)
#
# get_ramp_rate = partitioned_string[1]
# get_dwell_time = partitioned_string[2]
# get_load = partitioned_string[3]
# get_displacement = partitioned_string[4]
# get_spring_constant = partitioned_string[5]
#
# # Verify
# if(get_mode[0] != "$" or cmd_string == ""):
#     pass
# else:
#     print("Validate here")
