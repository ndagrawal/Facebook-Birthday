#!/bin/python
import facebook

oauth_access_token = "CAACEdEose0cBAJRZB6TZCcMH0zk9yKqElp4RDHZCJltSuR0BDylZCFKQksX77FgOXtFuVd064dw39KktOssrWvFUuzGunZCZBzyFNX8RgvNI6G8TNXUnxfPfeZCepZAZAuuqlz1pRCi2GlR0OmYQFwZBqCu4BlzfwwuxNzJZCtyTepVNW5ZC380EUCRRasnZBXXiM4a8ZD"
graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
feed = graph.get_object("me/feed")
data = feed["data"]

for x in data:
  print x["updated_time"] ,"=>", x["from"]["name"] , "=>", x["message"],"=>", x["id"]




#for x in data:
#  print x["id"]
#print profile["username"]
#feed = json.loads(feed_json)
#json_string = json.dumps(feed,sort_keys=True,indent=2)
#print json_string
#print "="*50
#print feed_json
#for x in feed:
#  print x 
#print feed;
print "="*50 
