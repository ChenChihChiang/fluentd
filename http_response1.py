from elasticsearch import Elasticsearch

import datetime

d1 = datetime.datetime.now()
#d3 = d1 + datetime.timedelta(minutes=-5)
d3 = d1 + datetime.timedelta(days=-5)

#print (d1.strftime("%Y-%m-%dT%H:%M:%S"))
#print (d3.strftime("%Y-%m-%dT%H:%M:%S"))

nowtime = d1.strftime("%Y-%m-%dT%H:%M:%S")
before5 = d3.strftime("%Y-%m-%dT%H:%M:%S")

#es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])
es = Elasticsearch([{'host': '10.0.0.11', 'port': '9200'}])

qdoc = {
  "query": {
    "bool": {
      "must": [
        {"match": {"response_code": "404"}},
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




fdoc = {
  "query": {
    "bool": {
      "filter":{
        "bool":{
          "must": [
            {"match_all": {}},
            #{"match": {"response_code": "404"}},
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


getdata = es.search(index="uat-nginx-access*", body=fdoc)

#print (getdata['hits']['total'])

m = getdata['hits']['total']

getdata = es.search(index="uat-nginx-access*", body=qdoc)

#print (getdata['hits']['total'])

s = getdata['hits']['total']

mm = float(m)
ss = float(s)
t = ss/mm*100
print (round(t,2))


#print (nowtime)
#print (before5)

