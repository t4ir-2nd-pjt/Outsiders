import googlemaps
import pandas as pd
import numpy as np

# google maps API Key
gmaps_key = "************"
gmaps = googlemaps.Client(key=gmaps_key)

# 위치 입력으로 경위도 출력
loc1 = input('첫번째 장소를 입력하세요.')
loc_info_1 = gmaps.geocode(f'{loc1}', language='ko')
loc2 = input('두번째 장소를 입력하세요.')
loc_info_2 = gmaps.geocode(f'{loc2}', language='ko')
loc3 = input('세번째 장소를 입력하세요.')
loc_info_3 = gmaps.geocode(f'{loc3}', language='ko')



loc_geo = loc_info_1[0].get("geometry")
lat1 = loc_geo['location']['lat']
lng1 = loc_geo['location']['lng']
loc_geo = loc_info_2[0].get("geometry")
lat2 = loc_geo['location']['lat']
lng2 = loc_geo['location']['lng']
loc_geo = loc_info_3[0].get("geometry")
lat3 = loc_geo['location']['lat']
lng3 = loc_geo['location']['lng']
print((lat1 + lat2 + lat3)/3)
print((lng1 + lng2 + lng3)/3)


# 지하철역 출력
# station_name = []
# station = pd.read_excel('subway_all.xlsx', encoding = 'utf-8')['역이름']
# for name in station:
#     station_name.append(name + '역')
# print(station_name)

# 지하철역 이름으로 경위도 출력하기
# for i in station_name:
#     station_info = gmaps.geocode(f'{i}', language='ko')
#     station_geo = station_info[0].get('geometry')
#     station_lat = station_geo['location']['lat']
#     station_lng = station_geo['location']['lng']
#     print(i, station_lat, station_lng)