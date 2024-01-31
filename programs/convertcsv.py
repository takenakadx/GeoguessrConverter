from ast import parse
from os import write
import requests
import json
import urllib.parse
import csv
import argparse

API_URL = 'https://maps.googleapis.com/maps/api/streetview/metadata?'

parser = argparse.ArgumentParser(description="このプログラムはGoolge Mapで立てたピンをGeoguessrのマップに変換する為のものです")

parser.add_argument("setting")
args = parser.parse_args()

with open(args.setting,"r") as f:
    jsondata = json.load(f)
    csvfiles = jsondata["loadfiles"]
    writepath = jsondata["writefile"]
    API_KEY = jsondata["API_KEY"]
    if API_KEY == "<API KEY>":
        print("APIキーを設定ファイルに追記してください")
        exit()

def get_streetview_coordinate(url,r=1000):
    path_tuple = urllib.parse.urlparse(url).path.split("/")
    if(path_tuple[2]=="place"):
        location_param = urllib.parse.unquote(path_tuple[3])
    elif(path_tuple[2]=="search"):
        location_param = path_tuple[3]
    param = {
        "key":API_KEY,
        "location":location_param,
        "radius":r
    }
    res = requests.get(API_URL,params=param).json()
    if(res["status"]=="OK"):
        return res["location"] #lat,lng
    else:
        print(location_param,"Not found!!")
        return None
    
def get_pins_from_csvfile(csvfilepath):
    resdata = []
    with open(csvfilepath,"r",encoding="utf-8") as f:
        next(csv.reader(f))
        csvreader = csv.reader(f)
        for elem in csvreader:
            coord = get_streetview_coordinate(elem[2])
            if(coord != None):
                resdata.append([coord["lat"],coord["lng"]])
            else:
                print("位置を見つけられませんでした : ",elem[2])
    return resdata

write_data = []

for loadpath in csvfiles:
    write_data.extend(get_pins_from_csvfile(loadpath))

with open(writepath,"w") as f:
    writer = csv.writer(f)
    writer.writerows(write_data)