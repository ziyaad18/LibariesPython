# this was practise
from datetime import datetime, timedelta

dt = datetime(2020, 10, 16, 11, 22, 50)
add_dt = dt+timedelta(days=5)
print(add_dt.strftime("%m-%d-%Y %H: %M: %S"))

from datetime import datetime, timedelta

current_date = datetime.now()
# this is exercise
# first attempt
for x in range(10):

      next_date = current_date + timedelta(days=14)

      current_date = next_date

      print(current_date.strftime("%Y:  %M: %D"))

# second attempt
from datetime import datetime, timedelta

thedate = datetime(2020, 10, 16,11, 5,8,12)

y=0

while y <10:
      print(thedate)
      thedate= thedate+timedelta(days=14)
      y=y+1

