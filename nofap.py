from datetime import datetime, timedelta
import time,threading, curses as c 
################################

######### INPUT ################
name = "Your name"
#No of days you want to quit
DAYS  = 30

FRAME = 0
#Time of Fapping
HOUR,MINUTE,SECOND = 15,22,0
#Date of Fapping
DAY,MONTH,YEAR = 23,5,2021

#################################

###### STARTING TIME  #####

START = datetime(YEAR, MONTH, DAY, HOUR,MINUTE,SECOND)

###### ENDING TIME   ######

CDAY = (START+timedelta(days=DAYS)).day
CMONTH = (START+timedelta(days=DAYS)).month

END = datetime(YEAR, CMONTH, CDAY, HOUR , MINUTE , SECOND)


###### Counting Time module ###
count = 0
back  = 0
days  = 0

def Counting():
	global count, back, days
	while True:
		count = END - datetime.now()
		back = abs(START - datetime.now())
		days = abs(back.days)

####### Percentage ######
perc = 0

def Percentage():
	global perc
	while True:
		seconds = (START - datetime.now()).total_seconds()
		total = (END - START).total_seconds()
		perc=round(abs(seconds/total)*100, 7)

######### RANKING #######


def Rank(perc):
	if perc < 1.0:
		rank = "NEWBIE"
	elif 1.0<perc<10.0:
		rank = "BEGINNER"
	elif 10.0<perc<20.0:
		rank = "STRONG MINDED"
	elif 20.0<perc<30.0:
		rank = "THE MONSTER"
	elif 30.0<perc<40.0:
		rank = "THE VETERAN"
	elif 40.0<perc<50.0:
		rank = "THE GENTLEMAN"
	elif 50.0<perc<60.0:
		rank = "THE KNIGHT"
	elif 60.0<perc<70.0:
		rank = "THE WARRIOR"
	elif 70.0<perc<80.0:
		rank = "THE LORD"
	elif 80.0<perc<90.0:
		rank = "THE MASTER"
	elif 90.0<perc<100.0:
		rank = "THE CONQUEROR"
	else:
		rank = "THE ALPHA"
	return rank
		

####### Threading #######

def Threading():
	count = threading.Thread(target = Counting)
	percentage = threading.Thread(target = Percentage)
	count.start()
	percentage.start()

###### Printing #######




def Printing():
	Threading()
	stdscr = c.initscr()
	c.start_color()
	c.init_pair(1,c.COLOR_RED,c.COLOR_BLACK)
	c.init_pair(2,c.COLOR_GREEN,c.COLOR_BLACK)
	c.init_pair(3,c.COLOR_BLACK,c.COLOR_WHITE)
	while True:
	    HEADING = f'''
#Nofap 
see {name}, you're going well

	 '''
	    DETAILS = f'''
	    
Completed:  {back}

Remaining: {count}

Days Completed: {days}/{DAYS}

TODAY: {datetime.now()}
'''
		
	    stdscr.erase()
	    stdscr.addstr(HEADING,c.A_BOLD)
	    stdscr.addstr('#### ' +Rank(perc)+' ####\n\n',  c.color_pair(1))
	    stdscr.addstr(f"  Brain Rewired: {perc}/100",c.color_pair(2))
	    stdscr.addstr(DETAILS)
	    
	    stdscr.refresh()
	    time.sleep(FRAME)

if __name__=="__main__":
	
	Printing()	    
	
	

