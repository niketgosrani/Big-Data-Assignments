print("A python program that (1) reads the contents of the above URL, (2) detect the presence of dates, and (3) count the number of events")

import urllib.request
import re

url = 'https://raw.githubusercontent.com/csula/cs594-spring-2015/master/Syllabus.md'

response = urllib.request.urlopen(url)
page = response.read()
print("\nRetrieved Data from URL in text format: \n", page)


# regular expression to match seasons in format: Spring|Summer|Fall|Winter
season_reg_exp = re.compile(r'\b(spring|summer|fall|winter)\b')
seasons = season_reg_exp.findall(str(page))
#print("\nSeasons :", seasons)
#print("Seasons Count:", len(seasons))

# regular expression to match dates in format: 08-10-2010 and 08/27/2010
year_reg_exp = re.compile(r"\b\d{4}\b")
year = year_reg_exp.findall(str(page))
#print("Year :", year)

date_len = len(year)
i = 0
for date_range in year:
    if '2000' <= date_range <= '2015':
        #print("Date:", date_range)
        i += 1
#print("Year", i)

# regular expression to match months in format: January|February|March|April|May|June|July|August|September|October|November|December
month_reg_exp = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b")
months = month_reg_exp.findall(str(page))
#print("Months :", months)
#print("Month Count:", len(months))

# regular expression to match dayOfTheWeek in format:Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
dayOfWeek_reg_exp = re.compile(r'\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b')
dayOfWeek = dayOfWeek_reg_exp.findall(str(page))
#print("Day of the week :", dayOfWeek)
#print("Day of the week:", len(dayOfWeek))

# regular expression to match Time in format: xx:xx am or xx:xx pm
time_reg_exp = re.compile(r'\d{1,2}(?:(?:am|pm)|(?::\d{1,2})(?:am|pm)?)')
time = time_reg_exp.findall(str(page))
#print("Time of the day :", time)
#print("Time of the day Count:", len(time))

date_reg_exp = re.compile(r'\b\d{1,2}[-/:]\d{1,2}[-/:]\d{4}\b')
date = date_reg_exp.findall(str(page))
#print("Date :", date)
#print("Date Count:", len(date))

print("\nReport :")
print("Seasons :", len(seasons))
print("Year :", i)
print("Day of the week :", len(dayOfWeek))
print("Time of the day :", len(time))
print("Date :", len(date))


