#Tech Academy python drill
#item 56 of 63

import datetime
import pytz


open = True

closed = False

ldn_hrs = ''
ptld_hrs = ''
nyc_hrs = ''

dt_utcnow = datetime.datetime.now(tz = pytz.UTC)

#def tmcnvrt(time):
#    if int(time)[:13] == 13:
#        newtime = time.replace(13, 1)
#    if int(time)[:13] == 14:
#        newtime = time.replace(14, 2)
#    if int(time)[:13] == 15:
#        newtime = time.replace(15, 3)
#    if int(time)[:13] == 16:
#        newtime = time.replace(16, 4)
#    if int(time)[:13] == 17:
#        newtime = time.replace(17, 5)
#    if int(time)[:13] == 18:
#        newtime = time.replace(18, 6)
#    if int(time)[:13] == 19:
#        newtime = time.replace(19, 7)
#    if int(time)[:13] == 20:
#        newtime = time.replace(20, 8)
#    if int(time)[:13] == 21:
#        newtime = time.replace(21, 9)
#    if int(time)[:13] == 22:
#        newtime = time.replace(22, 10)
#    if int(time)[:13] == 23:
#        newtime = time.replace(23, 11)
#    if int(time)[:13] == 24:
#        newtime = time.replace(24, 12)
#        
#    return newtime
#    
#
#
#
#for tz in pytz.all_timezones:
#    print tz
    



#check the time of portland timezone, set it to a varaible
dt_ptld = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
ptldTime = dt_ptld.strftime('%I:%M-%p')
#print "ptldTime = {} ".format(ptldTime)
#print ptldTime[:2], " ", ptldTime[6:8]
ptldHr = ptldTime[:2]
ptldM = ptldTime[6:8]
#print type(ptldTime)

dt_nyc = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
#nycTime = str((dt_nyc)[11:19])
nycTime = dt_nyc.strftime('%I:%M-%p')
#print "nycTime = {} ".format(nycTime)
nycHr = ptldTime[:2]
nycM = ptldTime[6:8]

dt_ldn = dt_utcnow.astimezone(pytz.timezone('Europe/London'))
ldnTime = dt_ldn.strftime('%I:%M-%p')
#print "ldnTime = {} ".format(ldnTime)
ldnHr = ldnTime[:2]
ldnM = ldnTime[6:8]

##check the saved time against the portland hours of operations
#if (int(ptldHr) in range(9, 12) and ptldM == 'AM') or (int(ptldHr) in range(1, 9) and ptldM == 'PM'):
#    ptld_hrs = open
#    print "portland office is open"
#else:
#    ptld_hrs = closed
#    print "portland office is closed"
#
#if (int(ldnHr) in range(9, 12) and ldnM == 'AM') or (int(ldnHr) in range(1, 9) and ldnM == 'PM'):
#    ldn_hrs = open
#    print "london office is open"
#else:
#    ldn_hrs = closed
#    print "london office is closed"
#
#if (int(nycHr) in range(9, 12) and nycM == 'AM') or (int(nycHr) in range(1, 9) and nycM == 'PM'):
#    nyc_hrs = open
#    print "NYC office is open"
#else:
#    nyc_hrs = closed
#    print "NYC office is closed"
#    
#if portland time between 9am and 9pm portland = open

#check the time in the timezone of nyc and london

#if nyc time between 9am and 9pm nyc = open

#if london time between 9am and 9pm london = open

#compare the status if zoneA == zoneB
print "#-"*20
print "The portland time is {}".format(str(dt_ptld)[11:19])
print "The portland time with timezone data is {}".format(str(dt_ptld))
print "Standard 12hr Portland Time = {} ".format(ptldTime)
if (int(ptldHr) in range(9, 12) and ptldM == 'AM') or (int(ptldHr) in range(1, 9) and ptldM == 'PM'):
    ptld_hrs = open
    print "Portland office is open"
else:
    ptld_hrs = closed
    print "portland office is closed"
print 
print "The london time is {}".format(str(dt_ldn)[11:19])
print "The london time with timezone data is {}".format(str(dt_ldn))
print "Standard 12hr London Time = {} ".format(ldnTime)
if (int(ldnHr) in range(9, 12) and ldnM == 'AM') or (int(ldnHr) in range(1, 9) and ldnM == 'PM'):
    ldn_hrs = open
    print "london office is open"
else:
    ldn_hrs = closed
    print "london office is closed"
print 
print "The New York time is {}".format(str(dt_nyc)[11:19])
print "The New York time with timezone data is {}".format(str(dt_nyc))
print "Standard 12hr NYC Time = {} ".format(nycTime)
if (int(nycHr) in range(9, 12) and nycM == 'AM') or (int(nycHr) in range(1, 9) and nycM == 'PM'):
    nyc_hrs = open
    print "NYC office is open"
else:
    nyc_hrs = closed
    print "NYC office is closed"
print "#-"*20

#print tmcnvrt(nycTime)