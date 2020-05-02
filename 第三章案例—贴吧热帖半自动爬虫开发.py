import re
import csv

with open('source.txt','r',encoding='UTF-8') as f:
	source=f.read()
	
result_list=[]
every_reply=re.findall('l_post l_post_bright j_l_post clearfix  "(.*?)p_props_tail props_appraise_wrap',source,re.S)

for each in every_reply:
	result={}
	result['username']=re.findall('username="(.*?)"',each,re.S)[0]
	result['content']=re.findall('j_d_post_content " style="display:;">(.*?)<',each,re.S)[0].replace('            ','')
	result['reply_time']=re.findall('class="tail-info">(20.*?)<',each,re.S)[0]
	result_list.append(result)
	
with open('tieba.csv','w',encoding='UTF-8-sig') as f:
	writer=csv.DictWriter(f,fieldnames=['username','content','reply_time'])
	writer.writeheader()
	writer.writerows(result_list)