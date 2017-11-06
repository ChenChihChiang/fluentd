GET /uat-nginx-access*/_search
{
  "query": {
    "bool": {
      "filter":{
        "bool":{
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
  }
}
