'''
Yiwen
05/01/2017
python crawl
Boston collision data 2016
final result
'''
import requests
import codecs
import csv
import re
import datetime
datalist=[]

# get the data from url
n=4538 # get the start id of the point
while n<=9228: # get the ending id of the point
    url1='http://gpd01.cityofboston.gov:6080/arcgis/rest/services/all_crashes_analysis/MapServer/6/query?f=json&where=Date%20LIKE%20%27%252016%25%27&returnGeometry=true&spatialRel=esriSpatialRelIntersects&&outFields=Incident, Date, Mode,Count&outSR=102100&objectIds='+str(n)
    res= requests.get(url1) # get the data
    select_result=[]
    result=re.findall(r"attributes\":{(.+?)]",res.content) #find the useful information
    str_result="".join(str(x) for x in result)
    result2=re.findall(r"Incident\":\"(.+?)\"|Date\":\"(.+?)\"|Mode\":\"(.+?)\"|Count\":(.+?)}",str_result)#find the information
    result3=re.findall(r"\"y\":(.+?)}",str_result) # get latitude
    result4=re.findall(r"\"x\":(.+?),",str_result) # get longitude
    for info in result2: # delete the data has no value
        c=0
        while c<4:
            if info[c]=="":
                pass
            else:
                if info[c] not in select_result:
                    select_result.append(info[c])
            c=c+1
    final_list=[]
    
    str2="".join(str(x) for x in select_result)
    str3="".join(str(x) for x in result3)
    str4="".join(str(x) for x in result4)
    select_result.append(str3)
    select_result.append(str4)
    final_list.append(select_result)
    for i in final_list:
        datalist.append(i) # append data into list
    n=n+1
for item in datalist:
    d=datetime.datetime.strptime(str(item[1]),"%m/%d/%Y %I:%M:%S %p") # split the time and date
    d1=str(d.month)+"/"+str(d.day)+"/"+str(d.year) # get date
    t1=str(d.hour)+":"+str(d.minute)+":"+str(d.second) #get time
    item[1]=d1
    item.insert(2,t1)
    
filename=r"C:\Users\yihu\Desktop\clean_data2.csv" # filepath and name

# write csv file
def writecsv(filename,data):
    fields=["Incident","Date","Time","Mode","Count","latitude","longitude"]
    with open(filename,"wb") as f:
        writer=csv.writer(f)
        writer.writerow(fields)
        for item in data:
            if item[4]=="0": # delete the data has no value
                item[4]=""
            writer.writerow(item)
    f.close()
    
print writecsv(filename,datalist)
print "done"
