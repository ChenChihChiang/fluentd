from elasticsearch import Elasticsearch
import datetime
import sys

code = sys.argv[1]
warning = int(sys.argv[2])
critical = int(sys.argv[3])
index = sys.argv[4]

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



getdata = es.search(index=sys.argv[4], body=mdoc)

m = float(getdata['hits']['total'])

getdata = es.search(index=sys.argv[4], body=sdoc)

s = (getdata['hits']['total'])

t = (round(s/m*100,2))


if t < critical:
   status = "CRITICAL"
   print ("%s status:%s (%s < %s) | status=%s;%s;%s;0;100" % (code, status, t, critical, t, warning, critical))
   sys.exit(2)
elif t < warning:
   status = "WARNING"
   print ("%s status:%s (%s < %s) | status=%s;%s;%s;0;100" % (code, status, t, warning, t, warning, critical))
   sys.exit(1)
else:
   status = "OK"
   print ("%s status:%s (%s > %s) | status=%s;%s;%s;0;100" % (code, status, t, warning, t, warning, critical))
   sys.exit(0)

#if t > critical:
#   status = "critical"
#elif t > warning:
#   status = "warning"
#else:
#   status = "ok"

