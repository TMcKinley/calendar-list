import datetime
import json
tzinfo = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
now = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0,tzinfo=tzinfo).isoformat()
#print(now)
#print(now.isoformat())
tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0,tzinfo=tzinfo).isoformat()
print(tomorrow)
#obj = obj.replace(tzinfo=tzinfo)
#print(json.dumps(datetime.datetime.now().isoformat()))
#print(datetime.datetime.now())
#print(datetime.datetime.utcoffset(datetime.datetime.now()))