#!/bin/python
import facebook
oauth_access_token = PUT YOUR TOKEN HERE 
graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
total_posts = 143
feed = graph.get_object("me/feed",limit=total_posts)
data = feed["data"]

Thanks = ["Thanks a lot :)","Thanks a ton!!","Thanks for the wishes!!"]
print "="*50
i = 0 
for x in data:
  i = i + 1
  message = x["message"]
#  sender= (x["from"]["name"])
#  try:
#    sender = unicode(sender, "utf-8")
#  except TypeError:
#    sender = unicode(sender, "ascii")
#  else:
#    # value was valid ASCII data
#    pass


#  value = unicode(sender, "utf-8")
#  print sender
  print x["updated_time"] ,"=>",  "=>", message ,"=>", x["id"] ,"=>" ,Thanks[i%3]
 # Like the post and write comments
  graph.put_like(x["id"])  
  graph.put_comment(x["id"],Thanks[i%3])  
print "="*50 
