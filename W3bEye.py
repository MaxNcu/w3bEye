#!/usr/bin/python3
# coding: utf-8
# Author: Yof3ng
# WebEye_1.0

import sys
import requests
import os
import optparse
import json
from optparse import OptionGroup

# def dict of true
Yes_dict = ['yes','Yes','Y','y']

# def request headers
headers = {
"Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
"Connection": "keep-alive",
"Content-Length": 22,
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Host": "tools.hexlt.org",
"Origin": "http://tools.hexlt.org",
"Referer": "http://tools.hexlt.org/subdomain",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
# def usage of w3beye
def parser_args():
	parser = optparse.OptionParser(
			usage="usage: ./%prog [-u] --url='http://xxxx.com'", version="W3bEye_1.0")
	parser.add_option('-u', '--url', dest='url', type='string', default=None,
			help='The url of target.')
	parser.add_option('-m','--myself',action='store_true',
			help='Network info of yourself.')	
	#Use OptionGroup，def the group of options
	group = OptionGroup(parser,'Expand Options',
                    'Remind: use these options to get designated info about your target.')
	#Add option
	group.add_option('-A','--AllExpand',action='store_true',
			help='Default choice: All information of target.')
	group.add_option('-H','--httpHeader',action='store_true',
			help='HttpHeader according to your target\'s.')
	group.add_option('-r','--reverseHackTarget',action='store_true',
			help='ReverseHackTarget according to your target.')
	group.add_option('-t','--traceRoute',action='store_true',
			help='TraceRoute according to your target.')
	group.add_option('-w','--whoIs',action='store_true',
			help='Whois.')
	group.add_option('-D','--dns',action='store_true',
			help='Look target\'s dns.')
	group.add_option('-N','--nmap',action='store_true',
			help='Nmap scan.')
	group.add_option('-R','--reverseDns',action='store_true',
			help='ReverseDns about target.')
	group.add_option('-F','--findSharedServer',action='store_true',
			help='Find shared server of target.')
	group.add_option('-G','--geoIp',action='store_true',
			help='Geoip of target.You can choose Yes or No.')
	group.add_option('-P','--pageLinks',action='store_true',
			help='Pagelinks of target.')
	# Add group to parser
	parser.add_option_group(group)
	(options, args) = parser.parse_args()
	return options,parser

# def banner color
def banner():
	if sys.platform.startswith('win'):
		P, B, Y, C, W ,R = '\033[1;95m', '\033[1;37m', '\033[1;33m', '\033[1;30m', '\033[0m','\033[1;31m'
		try:
			import win_unicode_console, colorama
			win_unicode_console.enable()
			colorama.init()
		except:
			print('[+] Error: Your operate system didn\'t installed the color modules!')
			P, B, Y, C, W, R = '', '', '', '', '',''
	else:
		P, B, Y, C, W ,R = '\033[1;95m', '\033[1;37m', '\033[1;33m', '\033[1;30m', '\033[0m', '\033[1;31m'

	# Banner of WebEye
	print('''%s
__        _______ _     _____           
\ \      / /___ /| |__ | ____|   _  ___ 
 \ \ /\ / /  |_ \| '_ \|  _|| | | |/ _ \ >| %s@Author: Yof3ng%s
  \ V  V /  ___) | |_) | |__| |_| |  __/ >| %s@Github: https://github.com/Yof3ng%s
   \_/\_/  |____/|_.__/|_____\__, |\___| >| %s@Version: W3bEye_1.0%s
                             |___/     
	 %s
--A tool for collecting information before attack.%s
'''%(R, P, R, P, R, P, R, Y,W))
		
def myself():
	try:
		print('[+] Start getting the host information...')
		resp=requests.get('http://www.ip-api.com/json/',timeout=3)
		myself_info = json.loads(resp.text)
		AS,CITY,COUNTRY,COUNTRY_CODE,ISP,LAT,LON,MYIP,regionName = myself_info['as'],myself_info['city'],myself_info['country'],myself_info['countryCode'],myself_info['isp'],myself_info['lat'],myself_info['lon'],myself_info['query'],myself_info['regionName']
		#print(myself_info[0])
		print('''[+] This is collecting from \'http://www.ip-api.com/\'... 
--------------------------------------------------------------
>|IP of mine:{7}                                  
>|City:{1}                               
>|Country:{2}/{3}                        
>|Isp:{4}                                
>|Lat:{5}                                
>|Lon:{6}                                
>|As: {0}                            
>|RegionName:{8}                         
--------------------------------------------------------------
	'''.format(AS,CITY,COUNTRY,COUNTRY_CODE,ISP,LAT,LON,MYIP,regionName ))
	
	except:
		print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
		
# Collecting url information from API of 'hackertarget.net'
class target_info:
	def __init__(self,target):
		self.target = target
	def httpHeader(self):
		print('[+]==> Starting get httpHeader...')
		try:
			baseApi = "http://api.hackertarget.com/httpheaders/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def reverseHackTarget(self):
		print('[+]==> Starting get reverseHackTarget info...')
		try:
			baseApi = "http://api.hackertarget.com/reverseiplookup/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def traceRoute(self):
		print('[+]==> Starting get traceRoute info...')
		try:
			baseApi = "http://api.hackertarget.com/mtr/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def whoIs(self):
		print('[+]==> Starting get whoIs info...')
		try:
			baseApi = "http://api.hackertarget.com/whois/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def dns(self):
		print('[+]==> Starting get dns...')
		try:
			baseApi = "http://api.hackertarget.com/dnslookup/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def reverseDns(self):
		print('[+]==> Starting get reverseDns info...')
		try:
			baseApi = "http://api.hackertarget.com/reversedns/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def geoIp(self):
		print('[+]==> Starting get geoIp info...')
		try:
			baseApi = "http://api.hackertarget.com/geoip/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def nmap(self):
		print('[+]==> Starting get nmap info...')
		try:
			baseApi = "http://api.hackertarget.com/nmap/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def findSharedServer(self):
		print('[+]==> Starting get findSharedServer...')
		try:
			baseApi = "http://api.hackertarget.com/findshareddns/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
	def pageLinks(self):
		print('[+]==> Starting get pageLinks...')
		try:
			baseApi = "http://api.hackertarget.com/pagelinks/?q=" + self.target
			base = requests.get(baseApi,timeout=10).text
			return base
		except:
			print('\033[1;31m'+'[!] Error...It seems that your network is not good!Please try again!'+'\033[0m')
			pass
def save_it(url,it):
	print(it)
	print("[+]==>Save it to file:"+url+".log")
	saveFile = open(url + '.log', 'a+')
	saveFile.write(it)
	saveFile.close()
def main():
	banner()
	options,parser =  parser_args()
	#print(options)
	if len(sys.argv)>1:
		if options.myself:
			myself()
		if (options.httpHeader or options.reverseDns or options.reverseHackTarget or options.traceRoute or options.whoIs or options.dns or options.geoIp or options.nmap or options.findSharedServer or options.pageLinks or options.AllExpand) and (options.url!=None):
			target = target_info(options.url)
			print('[+] Starting collect information of \'{}\'...'.format(options.url))
			if options.httpHeader:
				save_it(options.url,target.httpHeader())
			if options.reverseDns:
				save_it(options.url,target.reverseDns())
			if options.reverseHackTarget:
				save_it(options.url,target.reverseHackTarget())
			if options.traceRoute:
				save_it(options.url,target.traceRoute())
			if options.whoIs:
				save_it(options.url,target.whoIs())
			if options.dns:
				save_it(options.url,target.dns())
			if options.geoIp:
				save_it(options.url,target.geoIp())
			if options.nmap:
				save_it(options.url,target.nmap())
			if options.findSharedServer:
				save_it(options.url,target.findSharedServer())
			if options.pageLinks:
				save_it(options.url,target.pageLinks())
			if (options.httpHeader or options.reverseDns or options.reverseHackTarget or options.traceRoute or options.whoIs or options.dns or options.geoIp or options.nmap or options.findSharedServer or options.pageLinks)==True and options.AllExpand:
				save_it(options.url,target.httpHeader())
				save_it(options.url,target.reverseDns())
				save_it(options.url,target.reverseHackTarget())
				save_it(options.url,target.traceRoute())
				save_it(options.url,target.whoIs())
				save_it(options.url,target.dns())
				save_it(options.url,target.geoIp())
				save_it(options.url,target.nmap())
				save_it(options.url,target.findSharedServer())
				save_it(options.url,target.pageLinks())
	
		else:
			print(parser.print_help())

	else:
		print(parser.print_help())	


if __name__=="__main__":
	main()
	



