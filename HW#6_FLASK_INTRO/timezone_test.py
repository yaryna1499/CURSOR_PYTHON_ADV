import pytz
from datetime import datetime

test = datetime.now(tz=pytz.timezone('Europe/Kiev')).strftime('%Y-%m-%d %H:%M:%S %Z%z')

print(test)

