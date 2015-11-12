from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response

from article.models import Article
from article.network import *
from article.crawler import *
from article.crform  import *

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

import urllib
import mysql.connector
import time

########################################################################################
#SEAL SEALSEAL SEALSEAL SEALSEAL SEAL SEAL SEAL SEAL SEALSEAL SEALSEAL SEALSEAL SEAL #
########################################################################################
##new lesson
def articles(request):
	return render_to_response('articles.html',{'articles':Article.objects.all()})
def article(request,article_id=1):
	return render_to_response('article.html',{'article': Article.objects.get(id = article_id)})
#Create a view here
def hello(request):
	name = "ethan"
	html = "<html>Hi %s, hello world</html>" % name
	return HttpResponse(html)
def hello_template(request):
	name = "ethan"
	t = get_template('hello.html')
	html = t.render (Context({'name':name}))
	return HttpResponse(html)
def hello_template_simple(request):
	name = 'ethan_simple'
	return render_to_response('hello.html', {'name': name})
class HelloTemplate(TemplateView):
	template_name = 'hello_class.html'
	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Mike'
		return context
########################################################################################	
	
#####view controller dashboard
def dashboard(request):
	name = 'ETHANs CRAWLER'
	dict = {}
	dict['subject']='null'
	dict['depth']=1	
	dict['city']='kansascity'
	if request.method == 'POST': #If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid():
			dict['subject']=form.cleaned_data['subject']
			dict['depth']=form.cleaned_data['message']
			dict['city']=form.cleaned_data['city']
	else:
		form = ContactForm()
	dict['form']=form
	dict.update(csrf(request))
	###BEGIN
	print 'Executing...'
	millis = int(round(time.time() * 1000))
	print millis
	table_string='CACHE_%d'%millis
	#cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='CRAWLER',port=8889)
	cnx = mysql.connector.connect(user='root', password='honor',host='localhost',database='CRAWLER',port=3306)
	cursor = cnx.cursor()
	search_string=dict['subject']
	city_string = dict['city']
	cursor.execute('DROP TABLE IF EXISTS `CRAWLER`.`%s`'%(table_string))
	cursor.execute('CREATE TABLE `CRAWLER`.`%s` (`PID` int(11) NOT NULL AUTO_INCREMENT,`TITLE` varchar(1000) DEFAULT NULL,`PRICE` varchar(45) DEFAULT NULL,`DATE` varchar(45) DEFAULT NULL,`URL` varchar(1000) DEFAULT NULL, PRIMARY KEY (`PID`), UNIQUE KEY `PID_UNIQUE` (`PID`)) ;'%(table_string))
	#print ('CREATE TABLE `CRAWLER`.`%s` (`PID` int(11) NOT NULL AUTO_INCREMENT,`TITLE` varchar(1000) DEFAULT NULL,`PRICE` varchar(45) DEFAULT NULL,`DATE` varchar(45) DEFAULT NULL,`URL` varchar(1000) DEFAULT NULL, PRIMARY KEY (`PID`), UNIQUE KEY `PID_UNIQUE` (`PID`)) ;'%(table_string))
	cnx.commit()
	#Purge the data
	cursor.execute('delete from `CRAWLER`.`%s`'%table_string)
	cnx.commit()
	for i in range(0,dict['depth']):###set to 1
		print i
		urlstring1="http://%s.craigslist.org/search/sss?s=%d&query=%s"%(city_string,(i*100),search_string)
		urlstring2="http://%s.craigslist.org"%(city_string)
		tblname=table_string
		log=CRAWLER(urlstring1,urlstring2,cursor,tblname)
		#print urlstring1
	cnx.commit()
	
	#####Now begin to analysis
	Superliststr=''
	cursor.execute("""
		select 
		price as castive,
		count(*) as count
		from %s
		where price < 40000 and Price <> "NA" AND PRICE > 0 group by castive
		order by CAST(castive AS unsigned) ASC
	"""%tblname)
	results = cursor.fetchall()
		
	for result in results:
		Superliststr=Superliststr +  ('[%s,%s],'%(result[0],result[1]))[:-1] + ','
	
	dict['SuperList']=Superliststr[:-1]
	dict['ProjectName']='new'
	Flatlist=[]
	FlatDictlist=[]
	cursor.execute("""
		select TITLE,PRICE,URL
		from %s		
		where price < 40000 and Price <> "NA" AND PRICE > 0 LIMIT 50
	"""%tblname)
	results = cursor.fetchall()
	for result in results:
		Flatlist.append([result[0],result[1],result[2]])
		FlatDictlist.append({'TITLE':result[0],'PRICE':result[1],'URL':result[2]})
	dict['Flatlist']=Flatlist
	dict['FlatDictlist']=FlatDictlist
	
	cursor.execute('DROP TABLE IF EXISTS `CRAWLER`.`%s`'%(table_string))
	cnx.commit()
	cursor.close()
	cnx.close()
	return render_to_response('index.html',dict)
	







####UNDER DEVELOPING		
def crawler_search(request):
	dict = {}
	dict['subject']='null'
	dict['depth']=1	
	dict['city']='kansascity'
	if request.method == 'POST': #If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid():
			dict['subject']=form.cleaned_data['subject']
			dict['depth']=form.cleaned_data['message']
			dict['city']=form.cleaned_data['city']
	else:
		form = ContactForm()
	dict['form']=form
	dict.update(csrf(request))
	###BEGIN
	print 'Executing...'
	
	#cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='CRAWLER',port=8889)
	cnx = mysql.connector.connect(user='root', password='honor',host='localhost',database='CRAWLER',port=3306)
	cursor = cnx.cursor()
	search_string=dict['subject']
	city_string = dict['city']
	table_string='crawler.YINIC_CRAWLER_CACHE'
	#Purge the data
	cursor.execute('delete from %s'%table_string)
	cnx.commit()
	for i in range(0,dict['depth']):###set to 1
		print i
		urlstring1="http://%s.craigslist.org/search/sss?s=%d&query=%s"%(city_string,(i*100),search_string)
		urlstring2="http://%s.craigslist.org"%(city_string)
		tblname=table_string
		log=CRAWLER(urlstring1,urlstring2,cursor,tblname)
		#print urlstring1
	cnx.commit()
	cursor.close()
	
	#####Now begin to analysis
	Superliststr=''
	cursor = cnx.cursor()
	cursor.execute("""
		select 
		price as castive,
		count(*) as count
		from YINIC_CRAWLER_CACHE
		where price < 40000 and Price <> "NA" AND PRICE > 0 group by castive
		order by CAST(castive AS unsigned) ASC
	""")
	results = cursor.fetchall()
		
	for result in results:
		Superliststr=Superliststr +  ('[%s,%s],'%(result[0],result[1]))[:-1] + ','
	
	dict['SuperList']=Superliststr[:-1]
	cursor.close()
	cnx.close()
	return render_to_response('google_search.html',dict)
	
	
	
	
	
	
	
	
	
	

		
def crawler(request):
	Superliststr_sum=''
	Superliststr=''
	cnx = mysql.connector.connect(user='root', password='honor',host='localhost',database='CRAWLER',port=3306)
	#cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='CRAWLER',port=8889)
	#cnx = mysql.connector.connect(user='root', password='password',host='173.194.87.70',database='CRAWLER',port=3306)
	cursor = cnx.cursor()
	cursor.execute('select PID, PRICE from YINIC_BIKE where price < 40000 and Price <> "NA" AND PRICE > 0 order by PID ASC')
	results = cursor.fetchall()
	for result in results:
		Superliststr=Superliststr + ('[%s,%s],'%(result[0],str(result[1])))[:-1] + ','
		Superliststr_sum=Superliststr_sum+ ('[%s,%s,null],'%(result[0],str(result[1])))[:-1] + ','
	#print Superliststr[:-1]
	dict = {}
	dict['SuperList']=Superliststr[:-1]
	
	
	
	Superliststr=''
	cursor.close()
	cursor = cnx.cursor()
	cursor.execute('select PID, PRICE from YINIC_PIANO where price < 40000 and Price <> "NA" AND PRICE > 0 order by PID ASC')
	results = cursor.fetchall()
	for result in results:
		Superliststr=Superliststr + ('[%s,%s],'%(result[0],str(result[1])))[:-1] + ','
		Superliststr_sum=Superliststr_sum+ ('[%s,null,%s],'%(result[0]+3000,str(result[1])))[:-1] + ','
	#print Superliststr[:-1]
	dict['SuperList_2']=Superliststr[:-1]
	
	
	Superliststr=''
	cursor.close()
	cursor = cnx.cursor()
	cursor.execute("""
	select sub_piano.castive,sub_piano.count,sub_bike.count
		from 
		(
		select 
		price as castive,
		count(*) as count
		from YINIC_PIANO
		where price < 40000 and Price <> "NA" AND PRICE > 0 group by castive 
		) sub_piano,
		(
		select 
		price as castive,
		count(*) as count
		from YINIC_BIKE
		where price < 40000 and Price <> "NA" AND PRICE > 0 group by castive
		) sub_bike
		where 
		sub_bike.castive=sub_piano.castive
		order by CAST(sub_piano.castive AS unsigned) ASC
	""")
	results = cursor.fetchall()
		
	for result in results:
		#print ('[%s,%s,%s],'%(result[0],result[1],result[2]))[:-1]
		Superliststr=Superliststr +  ('[%s,%s,%s],'%(result[0],result[1],result[2]))[:-1] + ','

	#print Superliststr[:-1]
	dict['SuperList_Curve']=Superliststr[:-1]
	
	
	#####Another one
	Superliststr=''
	cursor.close()
	cursor = cnx.cursor()
	cursor.execute("""
		select 
		price as castive,
		count(*) as count
		from YINIC_CRAWLER_CACHE
		where price < 40000 and Price <> "NA" AND PRICE > 0 group by castive
		order by CAST(castive AS unsigned) ASC
	""")
	results = cursor.fetchall()
		
	for result in results:
		#print ('[%s,%s,%s],'%(result[0],result[1],result[2]))[:-1]
		Superliststr=Superliststr +  ('[%s,%s],'%(result[0],result[1]))[:-1] + ','

	#print Superliststr[:-1]
	dict['SuperList_Curve2']=Superliststr[:-1]
	#print Superliststr_sum[:-1]
	cursor.close()
	cnx.close()
	
	
	 #['x', 'Bike', 'Pano'],
     #[1, null, null],
	
	dict['SuperList_Sum']=Superliststr_sum[:-1]
	
	return render_to_response('googlechart2.html',dict)
	
	
	
	
	
	
	

def google(request):
	dict = {}
	dict['ETHAN']=175
	dict['ONIONS']=99
	dict['OLIVES']=2010
	dict['ZUCC']=40
	dict['PEP']=100
	dict['name']='TEST page'
	dict['title']='The first chart from Ethan'
	
	#A1 Perspective A1-A2,Truth
	A1_L12=10
	
	#A1 Perspective A2-A1,Expectation
	A1_L21=10
	
	#A2 Perspective A2-A1,Truth
	A2_L21=0
	
	#A2 Perspective A1-A2,Expectation
	A2_L12=5
	
	
	
	Mt=0
	MisJudgeAdaptRate=0.2
	PsyTruthAdaptRate=1.2
	Result_List=[A1_L12,A1_L12,A1_L21,A1_L21,A2_L12,A2_L12,A2_L21,A2_L21]
	for item in Result_List:
		print item
	print "===>>>>"
	
	
	SuperMtList=[]
	
	for i in range(40):
		Result_List=MisJudgement_Adapt_To_Truth(Result_List,MisJudgeAdaptRate) #Time2
		#Mt=abs(A1_L12-A2_L12)+abs(A1_L21-A2_L21)
		Mt=abs(Result_List[1]-Result_List[5])+abs(Result_List[3]-Result_List[7])
		print Mt
		SuperMtList.append([i,Mt])
		Result_List=PsyTruth_Adapt_To_Truth(Result_List,PsyTruthAdaptRate)
		Mt=abs(Result_List[1]-Result_List[5])+abs(Result_List[3]-Result_List[7])
		print Mt
		SuperMtList.append([i,Mt])
	
	dict['SuperList']=str(SuperMtList)[1:-1]
	return render_to_response('googlechart.html',dict)

	
	
	
	
	
