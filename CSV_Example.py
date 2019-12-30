#!/uar/bin/python
import csv
import pprint

f = open("country.csv", "r")
content = csv.reader(f)
for row in content:
    print(row)

f.seek(0)
index = {'name': 0, 'population': 1, 'capital': 2, 'citypop': 3, 'continent': 4, 'ind_date': 5,
         'currency': 6, 'religion': 7, 'language': 8}

content = csv.DictReader(f, fieldnames=list(index.keys()))

for row in content:
    pprint.pprint(row)

# csv module escapes commas automatically
row = ['python,', 'course', 'december']
f = open("country_results.csv", 'w')
csv_writer = csv.writer(f)
csv_writer.writerow(row)
f.close()
