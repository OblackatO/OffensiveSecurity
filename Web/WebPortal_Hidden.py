#!/usr/bin/env python
import urllib.request as ur
import argparse,sys,re

list1 = ['dashboard','robots.txt','admin','config']
file1 = open('PublicHosts_Info.txt','w')
file1.close()

def analyse_site(website):
	passed= False
	website = website+'/'
	set1 = 'http://'
	set2 = 'https://'
	try:
		domain = set1+website
		pre_rq = ur.Request(domain,headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"},method='HEAD')
		rq = ur.urlopen(pre_rq)
		hd = rq.info()
		print('[>]Available web portal: '+domain)
	except:
		print('[!]Web portal: '+domain+' not available.')
		hd = False
	try:
		domain2 = set2+website
		pre_rq = ur.Request(domain2,headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"},method='HEAD')
		rq = ur.urlopen(pre_rq)
		hd1 = rq.info()
		print('[>]Available web portal: '+domain2)
		passed = True
	except:
		print('[!]Web portal: '+domain2+' not available.')
		hd1 = False
	if (hd != False) or (hd1 != False) :
		file1 = open('PublicHosts_Info.txt','a')
		file1.write('\n'+'[>]Web portal: '+website+' is available'+'\n')
		print('[>]Checking for more info about '+website)
		if passed == True:
			check_d = domain2
			file1.write('[>]HEAD: '+'\n'+str(hd1)+'\n')
		if passed == False:
			check_d = domain
			file1.write('[>]HEAD: '+'\n'+str(hd)+'\n')
		file1.close()
		fixed_d2 = check_d
		for item in list1 :
			try:
				check_d = fixed_d2+item
				pre_rq = ur.Request(check_d,headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"})
				rq = ur.urlopen(pre_rq)
				head = rq.read().decode()
				file1 = open('PublicHosts_Info.txt','a')
				file1.write('[>]Web portal: '+website+' results for: '+item+' :'+'\n')
				file1.write(str(head)+'\n')
				file1.close()
			except:
				print('[!]Web portal: '+website+' has no results for: '+item)

def main_arguments():
	usage= sys.argv[0]+ ' will search for hidden locations on a website, use -Info option to see these locations.\
 The user can add more locations to be scanned if needed. Various web portals can be specified at the same time, the positive results\
 will be output into a txt file, the negative ones will be printed out in the command-line.'+'\n'+\
 '\n'+'Examples :'+'\n'+"'"+sys.argv[0]+' -Portals www.google.lu 31.13.64.35 www.rtl.lu -Addloc hiddenfolder1 hiddenfolder2'+"'"\
 +'\n'+"'"+sys.argv[0]+' -Portals 2001:0db8::0001 www.wort.lu'+"'"+'\n'+"'"+sys.argv[0]+' -Portals www.govcert.lu -Addloc hidden1'+"'"+'\n'+\
 'IPv6 should work just fine if your network is configured to use it, but it was never tested. An url can be specified or\
 an IP, like in the examples. The diferent hosts or aditional locations do not need to be separated with commas, spaces are enough.\
 Any suggestions, ideas, or negative and constructive criticism are greatly appriciated.'
	epilog = '\n'+"'"+'I have no special talents. I am only passionately curious.'+"'"+' Albert Einstein'
	parser = argparse.ArgumentParser(usage=usage,epilog=epilog)
	parser.add_argument('-Portals',metavar='-p',help='Various or only one website to be checked.',nargs='+')
	parser.add_argument('-Addloc',metavar='-a',help='One or more locations that the user would like to add.',nargs='+')
	parser.add_argument('-Info',help='Prints the locations that are going to be scanned.',action='store_true')
	arguments,unknown_args = parser.parse_known_args()
	if unknown_args:
		print('[!]Uknown arguments were specified.')
		sys.exit('[!]Details: '+str(unknown_args))
	if arguments.Info :
		for item in list1:
			print('[>]'+item)
	if arguments.Portals and arguments.Addloc:
		for loc in arguments.Addloc:
			list1.append(loc)
		for portal in arguments.Portals:
			if 'www' not in portal and '.' in portal : 
				analyse_site(portal)
			elif 'www' in portal:
				portal = portal.strip('www.')
				analyse_site(portal)
			elif ':' in portal:
				print('IPv6 Web portal detected.')
				analyse_site(portal)
			elif re.search("[0-9]{3}\.|[0-9]{2}\.",str(portal)) is not None:
				print('IPv4 Web portal detected.')
				analyse_site(portal)
			else:
				print('[!]Not able to scan Web portal:'+str(portal))
			
main_arguments()
				
