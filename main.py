import pytz,datetime

#Asking for user to add the year , month , day,hour and minute of that day
# Work on GMT (Greenwich mean Time)
year = int(input("Enter the year"))
month = int(input("Enter the month"))
day = int(input("Enter the day"))
hr  = int(input("Enter the hours"))
minute =int(input("Enter the minute"))

#Asking for the continent country or city
# example : "Africa/cairo" or "UTC" for london and "Asia/Kolkata" for India
continent = input("Name of the continent")
country = input("Enter the country or city to find ")

continent = continent.title()
country  = country.title()

user_time = datetime.datetime(year,month,day,hr,minute)


country_name = continent+"/"+country
# Any country time

country_timezone = pytz.timezone(country_name) 
country_time = pytz.utc.localize(user_time).astimezone(country_timezone)


print(country_time.isoformat())
