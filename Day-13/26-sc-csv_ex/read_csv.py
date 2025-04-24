import csv

with open(r'C:\Users\292905\Desktop\Python semicon\Day-13\26-sc-csv_ex\data.csv','r') as f:
  data = csv.reader(f)
  print('DATA TYPE: ', type(data))
  for row in data:
        print(row)

# Empty list [] -- beacuse of blank part in data.csv

reader = csv.DictReader(open(r"C:\Users\292905\Desktop\Python semicon\Day-13\26-sc-csv_ex\data.csv"))
## Can give you dictionory
for raw in reader:
    print(dict(raw))
