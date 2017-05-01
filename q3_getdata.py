'''
Yiwen
04/29/2017
python crawl
Boston collision data 2016
'''
import requests
import codecs
import csv
import re

datalist=[]

n=4538
while n<=9228:
    url1='http://gpd01.cityofboston.gov:6080/arcgis/rest/services/all_crashes_analysis/MapServer/6/query?f=json&where=Date%20LIKE%20%27%252016%25%27&returnGeometry=true&spatialRel=esriSpatialRelIntersects&&outFields=Incident, Date, Mode,Count&outSR=102100&objectIds='+str(n)
    res= requests.get(url1)
    select_result=[]
    result=re.findall(r"attributes\":{(.+?)}]",res.content)
    datalist.append(result)
    n=n+1

filename=r"C:\Users\yihu\Desktop\NY_interview_quesions\getdata.csv"
def writecsv(filename,data):
    with open(filename,"wb") as f:
        writer=csv.writer(f,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in data:
            writer.writerow(item)
    f.close()

print writecsv(filename,datalist)
print "done"
