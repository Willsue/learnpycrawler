import math
import random

history={}

def show_history():	
	for name,data in history.items():
			print('用户{}，记录如下{}'.format(name,data))
			
def start():
	name=input('请输入用户名称：')
	if name=='退出':
		return
	if name not in history:
		history[name]=[]
	answer=random.randint(0,1024)
	print(answer)
	try_to_guess(name,answer)

def try_to_guess(name,answer):
	try_num=0
	max_try_num=math.log2(1024)
	while try_num<max_try_num:
		guess_answer=int(input('请输入一个数字：'))
		if guess_answer<answer:
			print('你输入的数字比正确答案小。')
		elif guess_answer==answer:
			print('回答正确！')
			history[name].append('成功')
			break
		else:
			print('你输入的数字比正确答案大。')
		try_num+=1
	else:
		print('猜错的次数太多，失败。')
		history[name].append('失败')

def default():
	print('输入错误！请重新输入')
	print('='*40)
	
if __name__=='__main__':
	select_dict={'1':show_history,'2':start,'3':exit}
while True:
	select=input('1.历史记录\n2.继续游戏\n3.退出游戏\n请输入数字选择：')
	select_dict.get(select,default)()
	

