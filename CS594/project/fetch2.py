from lxml import html
import requests
import re
import json
from bs4 import BeautifulSoup
import time
import sys
import numpy as np

startTime = time.time()
page = requests.get("http://www.disastercenter.com/crime/uscrime.htm")

tree = html.fromstring(page.text)


tables = [tree.xpath('//table/tbody/tr[2]/td/center/center/font/table/tbody'),
          tree.xpath('//table/tbody/tr[5]/td/center/center/font/table/tbody')]

tabs = []

for table in tables:
    tab = []
    for row in table:
        for col in row:
            var = col.text_content()
            var = var.strip().replace(" ", "")
            var = var.split('\n')
            if re.match('^\d{4}$', var[0].strip()):
                tab_row = {}
                tab_row["Year"] = var[0].strip()
                tab_row["Population"] = var[1].strip()
                tab_row["Total"] = var[2].strip()
                tab_row["Violent"] = var[3].strip()
                tab_row["Property"] = var[4].strip()
                tab_row["Murder"] = var[5].strip()
                tab_row["Forcible_Rape"] = var[6].strip()
                tab_row["Robbery"] = var[7].strip()
                tab_row["Aggravated_Assault"] = var[8].strip()
                tab_row["Burglary"] = var[9].strip()
                tab_row["Larceny_Theft"] = var[10].strip()
                tab_row["Vehicle_Theft"] = var[11].strip()
                tab.append(tab_row)
    tabs.append(tab)

json_data = json.dumps(tabs, indent=4)

output = open("output.json", "w")
output1 = open("output.txt", "w")
print "    -> output.txt & output.json created()."
output.write(json_data)
output1.write(json_data)
print "    -> Finished."
print "    -> Total Time to write a file = %.3f" % (time.time() - startTime), "seconds."
output.close()

 # ---- finding mean of list ----- #
data = []  # Creates an empty list to store the numbers in
print("This program will make mean, median and mode very easy!")
print("\nFirst, we need to enter some numbers!")

num = input("Type your first number: ")
while num:
    data.append(float(num)) #Converts num into a float so we can do division
    print("\n", data)
    num = input("Add another number, or press enter to move on.")

#Work out the mean
total = sum(data)
length = len(data)
print("\n\nThe Mean Is:",total/length)

