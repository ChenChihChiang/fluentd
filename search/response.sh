GET /uat-nginx-access*/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {"response_code": "404"}},
        {"range": {
          "@timestamp": {
            "gte": "2017-11-01T00:00:00+08:00",
            "lte": "2017-11-01T23:59:59+08:00"}
          }
        }
      ]
    }
  }
}
