#!/usr/bin/env python
#
#  analyze_time.py
#  
#  This script will analyze my monthly summarys and output
#  a list of the number and percentage of time I spent on 
#  each project.
#
#  Created by Elena Long on 09/04/13.
#

#import urllib2
import os
import os.path
#from httplib import HTTP
#from urlparse import urlparse

# The variable below defines which files you want to look at


# This big block removes old analysis files and opens up clear, new ones
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if (os.path.exists("./monthly_analysis.txt")): os.remove("./monthly_analysis.txt")
monthlySummary = open("./monthly_analysis.txt","a")
if (os.path.exists("./daily_analysis.txt")): os.remove("./daily_analysis.txt")
dailySummary = open("./daily_analysis.txt","a")
if (os.path.exists("./meeting_analysis.txt")): os.remove("./meeting_analysis.txt")
meetingSummary = open("./meeting_analysis.txt","a")
if (os.path.exists("./test.txt")): os.remove("./test.txt")
testFile = open("./test.txt","a")

if (os.path.exists("./EG4list.txt")): os.remove("./EG4list.txt")
EG4list = open("./EG4list.txt","a")
if (os.path.exists("./g2plist.txt")): os.remove("./g2plist.txt")
g2plist = open("./g2plist.txt","a")
if (os.path.exists("./Lablist.txt")): os.remove("./Lablist.txt")
Lablist = open("./Lablist.txt","a")
if (os.path.exists("./b1list.txt")): os.remove("./b1list.txt")
b1list = open("./b1list.txt","a")
if (os.path.exists("./Azzlist.txt")): os.remove("./Azzlist.txt")
Azzlist = open("./Azzlist.txt","a")
if (os.path.exists("./QElist.txt")): os.remove("./QElist.txt")
QElist = open("./QElist.txt","a")
if (os.path.exists("./Doclist.txt")): os.remove("./Doclist.txt")
Doclist = open("./Doclist.txt","a")
if (os.path.exists("./CPlist.txt")): os.remove("./CPlist.txt")
CPlist = open("./CPlist.txt","a")
if (os.path.exists("./SysAdminlist.txt")): os.remove("./SysAdminlist.txt")
SysAdminlist = open("./SysAdminlist.txt","a")
if (os.path.exists("./JIlist.txt")): os.remove("./JIlist.txt")
JIlist = open("./JIlist.txt","a")
if (os.path.exists("./Olist.txt")): os.remove("./Olist.txt")
Olist = open("./Olist.txt","a")
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("Analyzing...\n")

# Below here we do the actual processing of the summaries
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

monthlySummary.write("Month	EG4	g2p	UNH Lab	b1	Azz	QE	Doc	Conf	JobI	Other	Total\n")
#year = 2013
for year in range (2013,2017):
		for month in range (1,13):
			thisMonth = "../monthly_summaries/"
			thisMonth += str(year)
			thisMonth += "-"
			if month < 10: 
				thisMonth += "0"
				thisMonth += str(month)
			elif month > 9: thisMonth += str(month)
			thisMonth += ".txt"
		#	print ("Processing month "+str(thisMonth))
			isEG4       = 0
			isg2p       = 0
			isLab       = 0
			isb1        = 0
			isAzz       = 0
			isQE        = 0
			isDoc       = 0
			isCP        = 0
			isJI        = 0
			isSysAdmin  = 0
			isO   = 0
			if (os.path.exists(thisMonth)):
				with open(thisMonth) as currentMonth:
					for num, line in enumerate(currentMonth, 1):
						if "EG4\n" in line and "	" not in line: 
							EG4line = num
							isEG4=1
						if "g2p\n" in line and "	" not in line: 
							g2pline = num
							isg2p=1
							isEG4=0
						if "UNH Lab\n" in line and "	" not in line: 
							Labline = num
							isLab=1
							isg2p=0
						if "b1\n" in line and "	" not in line: 
							b1line = num
							isb1=1
							isLab=0
						if "Azz\n" in line and "	" not in line: 
							Azzline = num
							isAzz=1
							isb1=0
						if "Quasi-Elastic 3He\n" in line and "	" not in line: 
							QEline = num
							isQE=1
							isAzz=0
						if "Papers and Grants\n" in line and "	" not in line: 
							Docline = num
							isDoc=1
							isQE=0
						if "Conference Planning\n" in line and "	" not in line: 
							CPline = num
							isCP=1
							isDoc=0
						if "SysAdmin\n" in line and "	" not in line: 
							SysAdminline = num
							isSysAdmin=1
							isCP=0
						if "Job Issues\n" in line and "	" not in line: 
							JIline = num
							isJI=1
							isSysAdmin=0
						if "Other\n" in line and "	" not in line: 
							Oline = num
							isO=1
							isJI=0
						if "\n" in line: endline = num
						if isEG4 is 1 and not line in ['EG4\n', '\r\n'] and line.strip(): EG4list.write(line)
						if isg2p is 1 and not line in ['g2p\n', '\r\n'] and line.strip(): g2plist.write(line)
						if isLab is 1 and not line in ['UNH Lab\n', '\r\n'] and line.strip(): Lablist.write(line)
						if isb1  is 1 and not line in ['b1\n', '\r\n'] and line.strip():  b1list.write(line)
						if isAzz is 1 and not line in ['Azz\n', '\r\n'] and line.strip(): Azzlist.write(line)
						if isQE  is 1 and not line in ['Quasi-Elastic 3He\n', '\r\n'] and line.strip():  QElist.write(line)
						if isDoc is 1 and not line in ['Papers and Grants\n', '\r\n'] and line.strip():  Doclist.write(line)
						if isCP  is 1 and not line in ['Conference Planning\n', '\r\n'] and line.strip():  CPlist.write(line)
						if isSysAdmin  is 1 and not line in ['SysAdmin\n', '\r\n'] and line.strip():  SysAdminlist.write(line)
						if isJI  is 1 and not line in ['Job Issues\n', '\r\n'] and line.strip():  JIlist.write(line)
						if isO   is 1 and not line in ['Other\n', '\r\n'] and line.strip():   Olist.write(line)
					numEG4       = g2pline       - EG4line       - 3
					numg2p       = Labline       - g2pline       - 3
					numLab       = b1line        - Labline       - 3
					numb1        = Azzline       - b1line        - 3
					numAzz       = QEline        - Azzline       - 3
					numQE        = Docline       - QEline        - 3
					numDoc       = CPline        - Docline       - 3
					numCP        = SysAdminline  - CPline        - 3
					numSysAdmin  = JIline        - SysAdminline  - 3
					numJI        = Oline         - JIline        - 3
					numO         = endline       - Oline         - 2
					numTotal = numEG4 + numg2p + numLab + numb1 + numAzz + numQE + numDoc + numCP + numSysAdmin + numJI + numO
					summaryLine = "{:.0f}/{:.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}	{:,.0f}\n".format(month,year,numEG4,numg2p,numLab,numb1,numAzz,numQE,numDoc,numCP,numSysAdmin,numJI,numO,numTotal)
					print (summaryLine)
					monthlySummary.write(summaryLine)
EG4list.close()
g2plist.close()
Lablist.close()
b1list.close()
Azzlist.close()
QElist.close()
Doclist.close()
CPlist.close()
SysAdminlist.close()
JIlist.close()
Olist.close()

EG4list      = open("./EG4list.txt","r")
g2plist      = open("./g2plist.txt","r")
Lablist      = open("./Lablist.txt","r")
b1list       = open("./b1list.txt","r")
Azzlist      = open("./Azzlist.txt","r")
QElist       = open("./QElist.txt","r")
Doclist      = open("./Doclist.txt","r")
CPlist       = open("./CPlist.txt","r")
SysAdminlist = open("./SysAdminlist.txt","r")
JIlist       = open("./JIlist.txt","r")
Olist        = open("./Olist.txt","r")
EG4all      = EG4list.readlines()
g2pall      = g2plist.readlines()
Laball      = Lablist.readlines()
b1all       = b1list.readlines()
Azzall      = Azzlist.readlines()
QEall       = QElist.readlines()
Docall      = Doclist.readlines()
CPall       = CPlist.readlines()
SysAdminall = SysAdminlist.readlines()
JIall       = JIlist.readlines()
Oall        = Olist.readlines()
EG4list.close()
g2plist.close()
Lablist.close()
b1list.close()
Azzlist.close()
QElist.close()
Doclist.close()
CPlist.close()
SysAdminlist.close()
JIlist.close()
Olist.close()


#dailySummary.write("Day		EG4	g2p	Lab	b1	Azz	QE	Doc	Conf	SysAdmin	JobI	Other	Total\n")
#year = 2013
for year in range (2013,2017):
		for month in range (1,13):
			for day in range (1,32):
				thisDay = "../daily_summaries/"
				thisDay += str(year)
				thisDay += "-"
				if month < 10: thisDay += "0"
				thisDay += str(month)
				thisDay += "/"
				thisDay += str(year)
				thisDay += "-"
				if month < 10: thisDay += "0"
				thisDay += str(month)
				thisDay += "-"
				if day < 10: thisDay += "0"
				thisDay += str(day)
				thisDay += ".txt"
				dayEG4 = 0
				dayg2p = 0
				dayLab = 0
				dayb1  = 0
				dayAzz  = 0
				dayQE  = 0
				dayDoc  = 0
				dayCP  = 0
				dayJI  = 0
				daySysAdmin  = 0
				dayO   = 0
				itemEG4 = 0
				itemg2p = 0
				itemLab = 0
				itemb1  = 0
				itemAzz = 0
				itemQE  = 0
				itemDoc  = 0
				itemCP  = 0
				itemSysAdmin  = 0
				itemJI  = 0
				itemO   = 0
				meetingEG4  = 0
				meetingg2p  = 0
				meetingLab  = 0
				meetingb1   = 0
				meetingAzz  = 0
				meetingQE   = 0
				meetingDoc  = 0
				meetingCP   = 0
				meetingSysAdmin   = 0
				meetingJI   = 0
				meetingO    = 0
				meetings    = 0.0
				notMeetings = 0
				notMeetingItems = 0
				itemTotal   = 0.0
				w = 0.000
				if (os.path.exists(thisDay)):
					currentDay = open(thisDay, 'r')
					dayList = currentDay.readlines()
					currentDay.close()
					found = False
					for dayLine in dayList:
						if not dayLine in "Daily Summary\n":
							testLine = "	"
							testLine += dayLine
							if testLine in EG4all: 
								itemEG4 = itemEG4 + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingEG4 = meetingEG4 + 1
									itemEG4 = itemEG4 - 1
							if testLine in g2pall: 
								itemg2p = itemg2p + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingg2p = meetingg2p + 1
									itemg2p = itemg2p - 1
							if testLine in Laball: 
								itemLab = itemLab + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingLab = meetingLab + 1
									itemLab = itemLab - 1
							if testLine in  b1all: 
								itemb1  = itemb1  + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingb1 = meetingb1 + 1
									itemb1 = itemb1 - 1
								if month is 3: testFile.write(testLine)
							if testLine in Azzall: 
								itemAzz = itemAzz + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingAzz = meetingAzz + 1
									itemAzz = itemAzz - 1
							if testLine in  QEall: 
								itemQE  = itemQE  + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingQE = meetingQE + 1
									itemQE = itemQE - 1
							if testLine in  Docall: 
								itemDoc  = itemDoc  + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingDoc = meetingDoc + 1
									itemDoc = itemDoc - 1
							if testLine in CPall: 
								itemCP = itemCP + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingCP = meetingCP + 1
									itemCP = itemCP - 1
							if testLine in  SysAdminall: 
								itemSysAdmin  = itemSysAdmin  + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingSysAdmin = meetingSysAdmin + 1
									itemSysAdmin = itemSysAdmin - 1
							if testLine in  JIall: 
								itemJI  = itemJI  + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingJI = meetingJI + 1
									itemJI = itemJI - 1
							if testLine in   Oall: 
								itemO   = itemO   + 1
								if "Meeting" in testLine or "meeting" in testLine:
									meetingO = meetingO + 1
									itemO = itemO - 1
							if "Meeting" in testLine or "meeting" in testLine:
								meetings = meetings + 1
				itemTotal = itemEG4 + itemg2p + itemLab + itemb1 + itemAzz + itemQE + itemDoc + itemCP + itemSysAdmin + itemJI + itemO
				if itemTotal > 0:
					w = (8-meetings)/itemTotal
				weightLine = "meetings = {:.0f}, itemTotal = {:.0f}, w = {:.2f}".format(meetings,itemTotal,w)
				print (weightLine)
				dayEG4      = w*itemEG4      + meetingEG4
				dayg2p      = w*itemg2p      + meetingg2p
				dayLab      = w*itemLab      + meetingLab
				dayb1       = w*itemb1       + meetingb1
				dayAzz      = w*itemAzz      + meetingAzz
				dayQE       = w*itemQE       + meetingQE
				dayDoc      = w*itemDoc      + meetingDoc
				dayCP       = w*itemCP       + meetingCP
				daySysAdmin = w*itemSysAdmin + meetingSysAdmin
				dayJI       = w*itemJI       + meetingJI
				dayO        = w*itemO        + meetingO
				dayTotal = dayEG4 + dayg2p + dayLab + dayb1 + dayAzz + dayQE + dayDoc + dayCP + daySysAdmin + dayJI + dayO
				notMeetings = dayTotal - meetings
#				summaryLine = "{:.0f}/{:.0f}/{:.0f}	{:.0f}	{:.0f}	{:,.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}\n".format(month,day,year,dayEG4,dayg2p,dayLab,dayb1,dayAzz,dayQE,dayCP,daySysAdmin,dayJI,dayO,dayTotal)
				summaryLine = "{:.0f}/{:.0f}/{:.0f}	{:.3f}	{:.3f}	{:,.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}\n".format(month,day,year,dayEG4,dayg2p,dayLab,dayb1,dayAzz,dayQE,dayDoc,dayCP,daySysAdmin,dayJI,dayO,dayTotal)
				meetingsLine = "{:.0f}/{:.0f}/{:.0f}	{:.3f}	{:.3f}	{:.3f}	{:.3f}\n".format(month,day,year,meetings,notMeetings,dayTotal,itemTotal)
#				meetingsLine = "{:.0f}/{:.0f}/{:.0f}	{:.0f}	{:.0f}	{:.0f}	{:.0f}\n".format(month,day,year,meetings,notMeetings,dayTotal,itemTotal)
				if day is 31:
					if month is 2 or month is 9 or month is 4 or month is 6 or month is 11: 
						summaryLine = ""
						meetingsLine = ""
				if month is 2 and day is 30: 
					summaryLine = ""
					meetingsLine = ""
				if month is 2 and day is 29 and not year%4 is 0: 
					summaryLine = ""
					meetingsLine = ""
				print (summaryLine)
				dailySummary.write(summaryLine)
				meetingSummary.write(meetingsLine)

	



print("All done!\n")





















