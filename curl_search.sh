curl -XPOST http://52.68.214.54:9200/uat-nginx-access*/_search?pretty=true -d '{"query": {
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
}'
