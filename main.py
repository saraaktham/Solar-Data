import pandas as pd
import numpy as np
import requests
import json

api_key = "1gHoGjlIGeXbQOpiunnlRrJS9vYYb490MA4n9X7s"
  # Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
# attributes = '[air_temperature,alpha,aod,asymmetry,cld_opd_dcomp,cld_reff_dcomp,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,dhi,dni,fill_flag,ghi,ozone,relative_humidity,solar_zenith_angle,ssa,surface_albedo,surface_pressure,total_precipitable_water,wind_direction,wind_speed]'
attributes = "wind_speed"
year = "2017"
# Set leap year to true or false. True will return leap day data if present, false will not.
leap_year = "false"
# Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 15, 30, 60.
interval = "60"
# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = "false"
full_name = "Sara%2BAbouelella"
email = "sabouelella3%40gatech.edu"
affiliation="student"
mailing_list = "false"
reason = "Academic"
lat, lon, year = 10.6416, 61.3995, 2019
ur, ul, dl, dr = (-102.063517, 41.005982), (-109.028849, 41.005982), (-109.094767, 37.082751), (-102.063517, 37.012603)

# wkt =  "POLYGON((41.005982 -102.063517,41.005982 -109.028849,37.082751 -109.094767,37.012603 -102.063517))"
x = 4
h_seg = (ur[1] - dr[1])/x
w_seg = abs(ur[0] - ul[0])/x
p1 = dl
url = "https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.json?api_key={}".format(api_key)
# print(url)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

for i in range(x):
  for i in range(x):
    p2 = p1[0] + h_seg, p1[1]
    p3 = p1[0] + h_seg, p1[1] + w_seg
    p4 = p1[0],  p1[1] + h_seg
    wkt = "POLYGON(({} {},{} {},{} {},{} {}))".format(p1[0],p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1])
    payload = "names={}&leap_day={}&interval={}&utc={}&full_name={}&email={}&affiliation={}&mailing_list={}&reason={}&attributes={}&wkt={}".format(year, leap_year, interval, utc, full_name, email, affiliation, mailing_list, reason, attributes, wkt)
    response = requests.request("GET", url, data=payload, headers=headers)
    print("*****************")
    print(response.text) 
    print("*****************")

    p1 = p2
  
  p1 = p1[0], p1[1] + w_seg 

    

# payload = "names={}&leap_day={}&interval={}&utc={}&full_name={}&email={}&affiliation={}&mailing_list={}&reason={}&attributes={}&wkt={}".format(year, leap_year, interval, utc, full_name, email, affiliation, mailing_list, reason, attributes, wkt)

# print(payload)


# df = pd.read_csv('https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=full_name, email=email, mailing_list=mailing_list, affiliation="student", reason=reason, api=api_key, attr=attributes), skiprows=2)


# response = requests.request("GET", url, data=payload, headers=headers)

# response.json()['outputs']['msg-iodc']

# print(response.text)