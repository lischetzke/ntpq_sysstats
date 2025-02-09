# import os
import os

hostname = "localhost"
debug = False

# execute command
data = os.popen("ntpq -c sysstats").read()

# parse the data
data = data.split("\n")

# remove empty lines
data = [line for line in data if line]

# split on :
data = [line.split(":") for line in data]

if debug:
    for i in range(len(data)):
        print(data[i])

# replace whitespace from first element with underscore
for i in range(len(data)):
    data[i][0] = data[i][0].replace(" ", "_")
    data[i][0] = data[i][0].lower()

if debug:
    for i in range(len(data)):
        print(data[i])

# second element, replace 3 whitespace with 2 whitespace while 3 whitespaces found
for i in range(len(data)):
    while "   " in data[i][1]:
        data[i][1] = data[i][1].replace("   ", "  ", 1)

for i in range(len(data)):
    data[i][1] = data[i][1].replace("  ", "", 1)

# split on 2 whitespaces
for i in range(len(data)):
    data[i][1] = data[i][1].split("  ")

# ignore uptime, control requests, sysstats reset
data = [line for line in data if line[0] != "uptime" and line[0] != "control_requests" and line[0] != "sysstats_reset"]

# keep relevant values
for i in range(len(data)):
    data[i][1] = data[i][1][0]

# output telegraf using format
for i in range(len(data)):
    print("ntp_sysstats,host={} {}={}".format(hostname, data[i][0], data[i][1]))
