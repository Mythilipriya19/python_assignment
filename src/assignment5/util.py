def datetime():
 from datetime import datetime
 date=input("Enter Date: ")
 date_str=datetime.strptime(date, "%d %m %Y")
 day=date_str.strftime("%A")
 return day

print(datetime())