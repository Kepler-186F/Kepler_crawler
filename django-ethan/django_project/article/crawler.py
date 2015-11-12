
import urllib
import mysql.connector

def CRAWLER(urlstring1,urlstring2,cursor,tblname):
	connection=urllib.urlopen(urlstring1)
	result=connection.read()

	result_A=result.find('<div class="content">')
	result_B=result.find('<div id="noresult_overlay"></div>',result_A+1)
	totalcontent=result[result_A:result_B]

	result_cut_A=totalcontent.find('<p class="row"')
	result_cut_B=totalcontent.find('</p>',result_cut_A+1)
	content=totalcontent[result_cut_A:result_cut_B]
	#print content
	#print '\n'

	while (result_cut_A!=-1):
		result_cut_A=totalcontent.find('<p class="row"',result_cut_B+1)
		result_cut_B=totalcontent.find('</p>',result_cut_A+1)
		content=totalcontent[result_cut_A:result_cut_B]
		#print content
		#print '\n'
		
		##Name
		name_a=content.find('class="hdrlnk">',1)
		name_b=content.find('</a>',name_a+1)
		name=content[name_a+15:name_b]
		#print name
		
		##Price
		price_a=content.find('<span class="price">',name_b+1)
		price_b=content.find('</span>',price_a+1)
		price=content[price_a+21:price_b]
		if price_a != -1:
			price = price
			#print price
		else:
			price = 'NA'
			#print price
		##Date
		date_a=content.find('<time datetime="',0)
		date_b=content.find('"',date_a+20)
		#print date_a,date_b
		date=content[date_a+16:date_b]
		#print date
		
		##URL
		url_a=content.find('<a href="',0)
		url_b=content.find('"',url_a+10)
		url=content[url_a+9:url_b]
		#print urlstring2+url
		#print '\n\n'
		url_final= urlstring2+url
		#print urlstring2+url
		#print '\n\n'
		url_final= urlstring2+url
		try:
			SQLPREPARE="insert into %s (TITLE,PRICE,DATE,URL) values ('%s','%s','%s','%s')"%(tblname,name.replace("'","*"),price,date,url_final)
			#print SQLPREPARE
			cursor.execute(SQLPREPARE)
		except:
			pass
	return 'FINISH!'
