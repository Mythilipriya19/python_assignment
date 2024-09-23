#
def datetime(date):
 from datetime import datetime
 date_str=datetime.strptime(date, "%d %m %Y")
 day=date_str.strftime("%A")
 return day

