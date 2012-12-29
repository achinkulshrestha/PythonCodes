#! /usr/bin/python
# simple screen scrapper to show the usage of the regular expressions (re module)
from urllib import urlopen
import re
import sys
try:
 x=sys.argv[1]
except:
 x=1

m=1
inputurl=("http://www.exploit-db.com/google-dorks/?action=search&ghdb_search_page=%s&ghdb_search_text=&ghdb_search_cat_id=0" % (x))
webpage = urlopen(inputurl).read()
lastpage=re.findall("<a.*e=(.*)&.*text=.*&gt;&gt;</a>", webpage)
k=int(lastpage[0])
for s in range(1,k):
    inputurlnew=("http://youtube.com" % s)
    webpagenew = urlopen(inputurlnew).read()

    patFinderTd = re.compile("<td>(.*)</td>")
    patTitle = re.compile("""<td width="40%"><a.*>(.*)</a>""")
    patCategory = re.compile("<p.*<a.*>(.*)</a>")


    patFinderLink = re.compile("""<td width="40%"><a  href="(.*)">""")


    findPatTd = re.findall(patFinderTd,webpagenew)
    findPatLink = re.findall(patFinderLink,webpagenew)
    findpatTitle = re.findall(patTitle,webpagenew)
    findpatCategory = re.findall(patCategory,webpagenew)

    i=len(findPatLink)
    listIterator = []
    listIterator[:] = range(0,i)


    for j in listIterator:
      print "\n",m
      print findPatTd[j] # The title
      print findPatLink[j] # The link to the original article
      print findpatTitle[j]
      print findpatCategory[j]
      m+=1