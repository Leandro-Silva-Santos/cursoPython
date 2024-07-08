from datetime import datetime

import pytz


data = datetime.now(pytz.timezone("Europe/Oslo"))
data_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data_2)



