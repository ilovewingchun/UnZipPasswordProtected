#!/usr/bin/python
'''
	Author: Tyler Chen (tyler@lastline.com / alphaone.tw@gmail.com)
	Version: 1.0
	Description: This program is designed to extract password protected Zip file(s) with certain algorithm.
	Usage: python unzip.py <zip file>
	Example: python unzip.py *.zip
'''
import sys
import os
import glob
from zipfile import ZipFile
file_fullname_list = sys.argv[1:]
file_basename_list = []
password_list = []
#Change this to your own keyword.
keyword = "infected"
#Change this to match the last(or beginning) of N character from filename.
position = -4

print "-"*80
print "This script will try to unzip file(s) using following password encryption algorithm:"
print "Keyword '%s' + last %s filename charcaters." %(keyword,abs(position))
print "If the file doesn't require any password, it will still be unzipped."
if len(sys.argv[1:]) == 0:
	print " [-] Error: You need to specify at least one zip file."
	sys.exit()
for i in file_fullname_list:
	file_basename_list.append(i.split(".")[-2])
for i in file_basename_list:
    password_list.append(i[position:])
password_list = [keyword + s for s in password_list ]

for i in range(len(password_list)):
	print "[+] Extracting malware sample %d/%d" %(i+1,len(password_list))
	try:
		ZipFile(file_fullname_list[i]).extractall(pwd=password_list[i])
		print "[+] Malware sample %s extracted." % file_basename_list[i]
		print "[*] Deleting %s!" % file_fullname_list[i]
	except Exception, e:
		print "-"*80
		print "[-] Error: %s - %s." % (e.filename, e.strerror)
		sys.exit()
	# Removing OS path
	try:
		os.remove(os.path.abspath(file_fullname_list[i]))
	except Exception, e:
		print "-"*80
		print "[-] Error: %s - %s." % (e.filename, e.strerror)
		sys.exit()
	print "[+] Moving on to next one...\n"
print "-"*80
print "[+] %s files extracted, good bye!\n" %len(password_list)
