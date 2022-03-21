import datetime

current_date = datetime.datetime.now()
# print("Current Date in DDMMYEAR : " + current_date.strftime('%d%m%Y'))
# print("Current Time in HH:MM:SS - " + current_date.strftime('%H:%M:%S'))

datetime_output = current_date.strftime('%d%m%Y %H:%M:%S')
print(datetime_output)

###################################################################
create_file_datetime_formate = current_date.strftime('%d%m%Y_%H%M%S')
filename01 = "Log_" + create_file_datetime_formate
filename02 = open(filename01, "w+")

###################################################################
# current_date02 = datetime.datetime.now(tz=datetime.timezone.utc)
current_date02 = datetime.datetime.now().astimezone(tz=datetime.timezone.utc)
print(current_date02)

###################################################################
find_day_of_date = datetime.datetime.today().strftime('%A')
print(find_day_of_date)

###################################################################
previous_date = datetime.datetime.today() - datetime.timedelta(days=4)
print(previous_date)
