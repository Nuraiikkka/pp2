#1 subtract five days
from datetime import timedelta, date
cur_date = date.today()
changed_date = cur_date - timedelta(days=5)
print(cur_date)
print(changed_date)

#2 yesterday, today, tomorrow
from datetime import timedelta, date
cur_date = date.today()
yes_date = cur_date - timedelta(days=1)
tom_date = cur_date + timedelta(days=1)
print(cur_date)
print(yes_date)
print(tom_date)

#3 microseconds from datetime
from datetime import datetime
with_micro = datetime.now()
print("with microseconds:", with_micro)
without_micro = with_micro.replace(microsecond=0)
print("without microseconds:", without_micro)

#4 two date difference in seconds
from datetime import datetime
first_date = datetime(2023,9,23, 12, 0, 0)
second_date = datetime(2023,9,23, 12, 20, 0)
dif_date = second_date - first_date
print(dif_date)
