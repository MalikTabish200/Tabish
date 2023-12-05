#WRITTEN BY MALIK TABISH
import requests
import os
import time
import sys

total =[]


def logo():
	os.system('clear')
	pass

def sep_and_save(sav,sep):
	os.system('touch /sdcard/123.txt')
	try:
		for choice_ids in sep:
			os.system('cat '+sav+' | grep "'+choice_ids+'" >> /sdcard/123.txt')
			os.system('sort -r /sdcard/123.txt | uniq > '+sav+'')
			os.system('rm -rf /sdcard/123.txt')
	except:pass
def main():
	logo()
	try:
		token= open ('token_eaa.txt','r',encoding='utf-8').read()
	except FileNotFoundError:
		login_cookie()
	print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
	print(42*'-')
	print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
	print("||||||||||  FACEBOOK  = MALIK TABISH")
	print("||||||||||  STATUS    = LEARNING")
	print("||||||||||  VERSION   = 0.1 \33[0;m ")
	print(42*'-')
	print (" [1] CREATE UNLIMITED FILE \n [2] REMOVE DUPLICATE AND SEPERATE LINKS \n [3] CHANGE TOKEN ")
	a = input(" (●) CHOOSE : ")
	if a == "1":
		dump(token)
	elif a == "2":
		logo()
		print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
		print(42*'-')
		print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
		print("||||||||||  FACEBOOK  = MALIK TABISH")
		print("||||||||||  STATUS    = LEARNING")
		print("||||||||||  VERSION   = 0.1 \33[0;m ")
		print(42*'-')
		print(' (●) EXAMPLE : 10001,61555 etc')
		sep = input(' (●) PUT DIGITS WITH COMMA : ').split(',')
		sav = input(' YOUR FILE PATH : ')
		sep_and_save(sav,sep)
		print(" YOUR FILE SAVED IN "+sav)
	else:os.system("rm -rf token_eaa.txt");main()
def dump(token):
	logo()
	global total
	ids_list = []
	os.system('rm -rf .a.txt')
	logo()
	
	print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
	print(42*'-')
	print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
	print("||||||||||  FACEBOOK  = MALIK TABISH")
	print("||||||||||  STATUS    = LEARNING")
	print("||||||||||  VERSION   = 0.1 \33[0;m ")
	print(42*'-')
	try:
		limit = int(input(' (●) HOW MANY IDZ YOU WANT TO DUMP : '))
	except:
		limit = 3
	for n in range(limit):
		ids_list.append(input(f' (●) PUT ID NO {n+1} : '))
	print(51*'-')
	sav = input(' (●) PUT FILE SAVE PATH : ')
	logo()
	print(51*'-')
	print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
	print(42*'-')
	print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
	print("||||||||||  FACEBOOK  = MALIK TABISH")
	print("||||||||||  STATUS    = LEARNING")
	print("||||||||||  VERSION   = 0.1 \33[0;m ")
	print(42*'-')
	for id in ids_list:
		json_prams = {
			'uid':id,
			'token':token,}
		posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_prams).json()
		
		try:
			status,data = posted['status'],posted['data']
			for accounts in data:
				node2 = accounts['node']
				# imnm = node2['name']
				imuid = node2['id']
				open('.a.txt', 'a', encoding='utf-8').write(imuid + '\n')
				idss = len(open('.a.txt','r').readlines())
				print(f'\r SUCESSFULLY : \033[93m{id} [{idss}]  \33[0;m  ')

		except Exception as e:
			status,msg = posted['status'],posted['message']
			if msg == 'You Have Used This Id Many Times . ':
				print(msg)
	file = open('.a.txt', 'r').read().splitlines()
	logo()
	print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
	print(42*'-')
	print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
	print("||||||||||  FACEBOOK  = MALIK TABISH")
	print("||||||||||  STATUS    = LEARNING")
	print("||||||||||  VERSION   = 0.1 \33[0;m ")
	print(42*'-')
	print(' (●) TOTAL ID TO EXTRACT '+str(len(file)))
	print(' (●) EXTRACTING FRIENDS OF FRIENDS ')
	print(42*'-')
	for uid in file:
		json_data2 = {
			'uid':uid,
			'token': token,}
		sys.stdout.write(f'\r CHECKING FRIENDLIST : \033[93m{uid}           \033[95m({len(total)}) \33[0;m ')
		sys.stdout.flush()
		posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_data2).json()
		try:
			status,data = posted['status'],posted['data']
			for accounts in data:
				node2 = accounts['node']
				open(sav, 'a', encoding='utf-8').write(node2['id'] + "|" + node2['name'] + '\n')
				total.append(str(node2['id']))
					
			print(f'\r SUCESSFULLY EXTRACTED: \033[93m{uid}    \33[0;m')

		except Exception as e:
			status,msg = posted['status'],posted['message']
			if msg == 'You Have Used This Id Many Times ':
				print(msg)
	print(51*'-')
	print("\r PROCESSS HAS BEEN COMPLETED ")
	print(" (●) REMOVE DUPLICATE AND SEPARATE ")
	print(' (●) EXAMPLE : 10001,61555 ETC')
	sep = input(' (●) PUT DIGITS WITH COMMA : ').split(',')
	sep_and_save(sav,sep)
	print(" YOUR FILE SAVED IN "+sav)



	
def login_cookie():
	print("""\033[93m
       ######## ##     ##  #######  
          ##     ##   ##  ##     ## 
          ##      ## ##   ##     ## 
          ##       ###    ##     ## 
          ##      ## ##   ##     ## 
          ##     ##   ##  ##     ## 
          ##    ##     ##  #######  \33[0;m
""")
	print(42*'-')
	print("\033[94m||||||||||  CREATOR   = MALIK TABISH")
	print("||||||||||  FACEBOOK  = MALIK TABISH")
	print("||||||||||  STATUS    = LEARNING")
	print("||||||||||  VERSION   = 0.1 \33[0;m ")
	print(42*'-')
	cok = input('\033[1;97m (●) PUT COOKIES : ')
	print(51*'-')
	json_data = {'cookie':cok}
	r = requests.get('https://dilutecodes.pythonanywhere.com//login-cookiev2',json=json_data).json()
	try:
		status,token = r['status'],r['token']
		if status == 'success':
			print('\033[1;92m [*] LOGIN SUCCESSFULL \033[1;97m')
			print(f' [*] YOUR TOKEN : \033[1;96m{token}\033[1;97m')
			open ('token_eaa.txt','w',encoding='utf-8').write(str(token))
			time.sleep(2)
			main()
		else:
			print(' COOKIES CHECKPOINT')
			print(r)
	except Exception as e:
		print(e)



main()