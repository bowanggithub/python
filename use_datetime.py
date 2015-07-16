import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt=re.match(r"^(\d{4})\-(\d*)\-(\d*)\s(\d{2}):(\d{2}):(\d{2})$",dt_str)
    tz=re.match(r"^UTC([+-])(\d{1,2}):00$",tz_str)
    print(dt.groups())
    print(tz.groups())
    if tz.group(1)=="+":
        tzone=int(tz.group(2))
    else:
        tzone=-int(tz.group(2))
    dtime=datetime(int(dt.group(1)),int(dt.group(2)),int(dt.group(3)),int(dt.group(4)),int(dt.group(5)),int(dt.group(6)),tzinfo=timezone(timedelta(hours=tzone)))
    print(dtime.timestamp())


t1=to_timestamp("2015-6-1 08:10:30", "UTC+7:00")
t2=to_timestamp("2015-5-31 16:10:30", "UTC-09:00")
