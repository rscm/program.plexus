# -*- coding: utf-8 -*-

""" p2p-streams (c) 2014 enen92 fightnight
   
   This file manages the history of recent played p2p addon items
   
   Functions:
   
    
"""
import xbmcvfs,xbmc,os,sys
from utils.pluginxbmc import *
from utils.iofile import *
from utils.directoryhandle import addDir

history_file = os.path.join(pastaperfil,'history.txt')

def list_history():
	if xbmcvfs.exists(history_file):
		lines = open(history_file).readlines()
		i=0
		for line in lines:
			info = line.split('|')
			print info
			try:
				addDir(info[0],info[1],int(info[2]),info[3].replace('\n',''),1,False)	
			except: pass
	else:
		sys.exit(0)
	
def add_to_history(name,url,mode,iconimage):
	line = str(name) + '|' + str(url) + '|' +str(mode) +'|' + str(iconimage) + '\n'
	if xbmcvfs.exists(history_file):
		lines = open(history_file).readlines()
		if len(lines) < int(settings.getSetting('items_per_page')):
			if name in lines[0]: pass
			else:
				lines.insert(0,line)
				open(history_file, 'w').writelines(lines)
		else:
			lines = open(history_file).readlines()
			newlines = lines[0:-2]
			newlines.insert(0,line)
			open(history_file, 'w').writelines(newlines)
	else:
		save(history_file,line)
	return
	
def remove_history():
	if xbmcvfs.exists(history_file):
		xbmcvfs.delete(history_file)
		xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % (translate(40000), translate(600026), 1,addonpath+"/icon.png"))
		