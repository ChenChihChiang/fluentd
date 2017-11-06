from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])

qdoc = {
  "query": {
    "bool": {
      "must": [
        {"match": {"response_code": "404"}},
        {"range": {
          "@timestamp": {
            "gte": "2017-11-06T00:00:00+08:00",
            "lte": "2017-11-07T23:59:59+08:00"}
          }
        }
      ]
    }
  }
}

getdata = es.search(index="uat-nginx-access*", body=qdoc)

print (getdata['hits']['total'])