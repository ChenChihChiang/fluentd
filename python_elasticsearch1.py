from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])

#http://52.68.214.54:9200/uat-nginx-access-20171027/access_log/AV9dBXyaUYNxzOaG0uA6

#getdata = es.get(index="uat-nginx-access-20171027", doc_type="access_log", id=AV9dBXyaUYNxzOaG0uA6)['_source']
#print '-------------------------'
#print 'get data <= ' 

#es.indices.refresh(index="uat-nginx-access-20171027")
