from datetime import timedelta, date
import numpy as np

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

dates = []
start_date = date(2012, 1, 1)
end_date = date(2017, 1, 1)
for single_date in daterange(start_date, end_date):
    dates.append(single_date.strftime("%m/%d/%Y"))

dates = np.asarray(dates)
dates_some = np.random.choice(dates, size=50)

print("{}".format(list(dates_some)))
