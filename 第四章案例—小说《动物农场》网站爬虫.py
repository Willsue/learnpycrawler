import requests
import re
import os
from multiprocessing.dummy import Pool

start_url='https://www.kanunu8.com/book3/6879/'

def get_source(url):
	html=requests.get(url).content.decode('GBK')
	return html

def get_toc(html):
	toc_url_list=[]
	toc_block=re.findall('正文(.*?)</tbody>',html,re.S)[0]
	top_url=re.findall('<a href="(.*?)">',toc_block,re.S)
	for url in top_url:
		toc_url_list.append(start_url+url)
	return toc_url_list

def get_article(html):
	chapter_name=re.search('size="4"> (.*?)<',html,re.S).group(1)
	text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)
	text_block=text_block.replace('<br />','')
	return chapter_name,text_block
	
def save(chapter,article):
	os.makedirs('动物农场',exist_ok=True)
	with open(os.path.join('动物农场',chapter+'.txt'),'w',encoding='utf-8') as f:
		f.write(article)

def query_article(url):
	article_html=get_source(url)
	chapter_name,article=get_article(article_html)
	save(chapter_name,article)
		
if __name__=='__main__':
	html=get_source(start_url)
	toc_url_list=get_toc(html)
	pool=Pool(5)
	pool.map(query_article,toc_url_list)
	