# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
from urllib import request 
import urllib


# change the url according to your own corename and query
#inurl = 'http://localhost:8983/solr/corename/select?q=*%3A*&fl=id%2Cscore&wt=json&indent=true&rows=1000'
#outfn = 'path_to_your_file.txt'
all_models = ['BM25','DFR','LM']
for model in all_models:
	with open("model_"+model+".txt", 'w') as outfn:
		with open("test_queries.txt", 'r') as aq:
			line = aq.readline()
			while line:
				line = line.strip('\n').replace(':',"")
				val = line.split(" ",1)

				qid = val[0]
				query = val[1]
				
				print(query)
				#query = urllib.parse.quote_plus(query)
				query_in_url = "text_ru: ("+query+")"+ "OR "+"text_en: ("+query+")"+"OR "+"text_de: ("+query+")"
				query1=urllib.parse.quote_plus(query_in_url)
				inurl = 'http://18.189.192.79:8983/solr/'+model+'/select?q='+query1+'&fl=id%2Cscore&wt=json&indent=true&rows=20'
				
				#IRModel='default'
				data = urllib.request.urlopen(inurl)

				docs = json.load(data)['response']['docs']
				rank = 1
				for doc in docs:
									
				    outfn.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model + '\n')
				    rank += 1
				
				line = aq.readline()
outfn.close()
