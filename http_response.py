from elasticsearch import Elasticsearch
import datetime
import sys

code = sys.argv[1]
warning = int(sys.argv[2])
critical = int(sys.argv[3])

d1 = datetime.datetime.now()
#d3 = d1 + datetime.timedelta(minutes=-5)
d3 = d1 + datetime.timedelta(days=-5)

nowtime = d1.strftime("%Y-%m-%dT%H:%M:%S")
before5 = d3.strftime("%Y-%m-%dT%H:%M:%S")

#es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])
es = Elasticsearch([{'host': '10.0.0.11', 'port': '9200'}])

mdoc = {
  "query": {
    "bool": {
      "filter":{
        "bool":{
          "must": [
            {"match_all": {}},
            {"range": {
              "@timestamp": {
                "gte": before5+"+08:00",
                "lte": nowtime+"+08:00"}
              }
            }
          ]
        }
      }
    }
  }
}


sdoc = {
  "query": {
    "bool": {
      "filter":{
        "bool":{
          "must": [
            {"match": {"response_code": code }},
            {"range": {
              "@timestamp": {
                "gte": before5+"+08:00",
                "lte": nowtime+"+08:00"}
              }
            }
          ]
        }
      }
    }
  }
}



getdata = es.search(index="uat-nginx-access*", body=mdoc)

m = float(getdata['hits']['total'])

getdata = es.search(index="uat-nginx-access*", body=sdoc)

s = (getdata['hits']['total'])

t = (round(s/m*100,2))


if t > critical:
   status = "critical"
elif t > warning:
   status = "warning"
else:
   status = "ok"


print ("%s percentage: %s | time=%s;70;80;0;100" % (code, status, t))
