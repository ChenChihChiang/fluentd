from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])


r = requests.get('http://52.68.214.54:9200')
i = 1
while r.status_code == 200:
   r = requests.get('http://swapi.co/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
   i=i+1
 
print(i)

