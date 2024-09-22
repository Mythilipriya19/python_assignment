def dt():
 from datetime import datetime
 date_time1= "Sat 08 May 2021 12:15:30 +0530"
 date_time2= "Sat 08 May 2021 14:30:15 +0000"
 date_strap1=datetime.strptime(date_time1, '%a %d %b %Y %H:%M:%S %z')
 date_strap2=datetime.strptime(date_time2, '%a %d %b %Y %H:%M:%S %z')
 time_diff=abs(date_strap1-date_strap2).total_seconds()
 return f"The difference in seconds is: {int(time_diff)} seconds"
print(dt())

