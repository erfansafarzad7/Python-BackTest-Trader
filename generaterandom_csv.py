
import datetime
import csv
import random
import pandas as pd

# create random value
records=1_000

fieldnames=['date','open','high', 'low', 'close']
writer = csv.DictWriter(open("data.csv", "w"), fieldnames=fieldnames)


writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('date', datetime.datetime(2000, 1, 1) + datetime.timedelta(days=i)),
    ('open', random.randint(1, 100_000)),
    ('high', random.randint(1, 100_000)),
    ('low', random.randint(1, 100_000)),
    ('close', random.randint(1, 100_000)),
  ]))




# delete blanks

df = pd.read_csv('data.csv')
df.to_csv('data2.csv', index=False)
