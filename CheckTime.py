from datetime import datetime, timedelta, timezone
import pytz
from dateutil.tz import gettz

dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
bus_time = []

def timecheck(df_list,i,time):
    for column in range(0, 4):
        for line in range(0, len(df_list[i])):

            bustime = str(dt_now.date()) + ' ' + df_list[i].iloc[line, column] + ':00'
            bustime = bustime.split('+')[0]
            bustime = datetime.strptime(bustime, '%Y-%m-%d %H:%M:%S')

            serchtime = str(dt_now.date()) + ' ' + time + ':00'
            serchtime = serchtime.split('+')[0]
            serchtime = datetime.strptime(serchtime, '%Y-%m-%d %H:%M:%S')

            jst_timedelta = timedelta(hours=+9)
            jst = timezone(jst_timedelta, 'JST')
            bustime = bustime.astimezone(jst)
            serchtime = serchtime.astimezone(jst)

            if serchtime.time() < bustime.time():
                bus_time.append(str(bustime.time()))
                break
    return bus_time
