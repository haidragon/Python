#!/usr/bin/python

import re
import sys
import os
import datetime
import commands
import traceback
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-p","--parameter",dest="parameter",help='''parameter [USD/Other/Quote]
                        USD    --- monitor USD/CNY Inverted Message
                        Other  --- monitor Other Inverted Message
                        Quote  --- monitor DATA-TSS-0010 Message''')

g_today = datetime.datetime.now().strftime('%Y%m%d')
(options,args)=parser.parse_args()
g_processlockfile='/tmp/invertedCheckProcessLock'
g_parameter=None
g_parafile='/tmp/fhdepcmdslogparameter'
g_logfile = None#MetaObject日志路径
g_oldlogdate=None
g_oldlogtell=None
g_lastreceivedtime=None
g_resultfile = None
g_key = None
g_keynormal = "--->received meta object:DATA-TSS-0010"
g_firstruntime = None

#logfile01 = os.path.expandvars('$HOME') + "/Composer/cmpr/data/FH_DEP_CMDS-01.MetaObj." + g_today + ".log"
#logfile02 = os.path.expandvars('$HOME') + "/Composer/cmpr/data/FH_DEP_CMDS-02.MetaObj." + g_today + ".log"
logfile01 = "/cmds/cmds_data1/FH_DEP_CMDS-01.MetaObj." + g_today + ".log"
logfile02 = "/cmds/cmds_data1/FH_DEP_CMDS-02.MetaObj." + g_today + ".log"

#根据不同服务器选择日志路径
if os.path.exists(logfile01):
        g_logfile = logfile01
elif os.path.exists(logfile02):
        g_logfile = logfile02
else:
        sys.exit()
#结果存放位置
resultdir = os.path.expandvars('$HOME') + "/tools/invertedlog/"
if not os.path.exists(resultdir):
        os.mkdir(resultdir)

if options.parameter != None:
        g_parameter = options.parameter
        g_parafile='/tmp/fhdepcmdslogparameter'+g_parameter
        if g_parameter == "Quote":
                g_processlockfile='/tmp/quoteCheckProcessLock'
                g_resultfile = resultdir + "QuoteStatus.log"# + g_today + ".log"
        else:
                g_processlockfile += g_parameter
                g_resultfile = resultdir + "inverted_" + g_parameter + ".log"# + g_today + ".log"
                if g_parameter != "USD" and g_parameter != "Other":
                        print "g_parameter error, Usage ./invertedCheck.py -h"
                        sys.exit()
                elif g_parameter == "USD":
                        g_parameter = "USDCNY"
else:
        print "Usage: ./invertedCheck.py -h"
        sys.exit()

if g_parameter == "Quote":
        g_key="--->received meta object:DATA-TSS-0010"
else:
        g_key="--->received Inverted Price("+g_parameter+")"

if os.path.exists(g_processlockfile):
        print "process is running, exit..."
        sys.exit()

def readparafile():
        global g_today
        global g_parafile
        global g_oldlogdate
        global g_oldlogtell
        global g_lastreceivedtime
        if os.path.exists(g_parafile):
                pf = open(g_parafile,'r')
                if g_parameter == "Quote":
                        for line in pf:
                                if line.startswith('FH_DEP_CMDS_LOG_DATE'):
                                        g_oldlogdate=line.split('=')[1].lstrip().rstrip()
                                elif line.startswith('FH_DEP_CMDS_LOG_TELL'):
                                        g_oldlogtell=line.split('=')[1].lstrip().rstrip()
                                elif line.startswith('LAST_RECEIVED_TIME'):
                                        g_lastreceivedtime=line.split('=')[1].lstrip().rstrip()
                else:
                        for line in pf:
                                if line.startswith('FH_DEP_CMDS_LOG_DATE'):
                                        g_oldlogdate=line.split('=')[1].lstrip().rstrip()
                                elif line.startswith('FH_DEP_CMDS_LOG_TELL'):
                                        g_oldlogtell=line.split('=')[1].lstrip().rstrip()
                pf.close()
        if g_oldlogdate == None:
                g_oldlogdate = g_today

        if g_oldlogdate != g_today:
                g_oldlogdate = g_today
                g_oldlogtell = None
                g_lastreceivedtime = None
                g_firstruntime = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')

def writelog(sMsg):
        if os.path.exists(g_resultfile):
                rf = open(g_resultfile,'a')
        else:
                rf = open(g_resultfile,'w')
        rf.writelines(sMsg)
        rf.close()

try:
        fl=open(g_processlockfile,'w')
        readparafile()

        fo=open(g_logfile,'r')
        if g_oldlogtell != None:
                fo.seek(int(g_oldlogtell))

        quotereceivedtime=None
        onlyInverted = False
        invertedmsg = ""
        inInverted = False
        line = fo.readline()
        while line:
                if g_parameter == "Quote":
                        if line.find(g_key) != -1:
                                quotereceivedtime=line.split(',')[0]
                elif not inInverted:
                        if line.find(g_key) != -1:
                                onlyInverted = True
                                invertedmsg = line.split(';',1)[0] + "\n"
                        elif line.find(g_keynormal) != -1:
                                onlyInverted = False
                                inInverted = True
                line = fo.readline()
        g_oldlogtell=str(fo.tell())
        fo.close()

        if g_parameter != "Quote" and onlyInverted == True:
                writelog(invertedmsg)

        pf = open(g_parafile,'w')
        pf.writelines('FH_DEP_CMDS_LOG_DATE='+g_today+'\n')
        pf.writelines('FH_DEP_CMDS_LOG_TELL='+g_oldlogtell+'\n')
        if g_parameter == "Quote":
                if quotereceivedtime != None:
                        pf.writelines('LAST_RECEIVED_TIME='+quotereceivedtime + '\n')
                else:
                        now = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
                        tmp = now.split('-')[1].split(':')
                        cbcd = int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])
                        lbcd = None
                        smsg = None
                        if g_lastreceivedtime != None:
                                pf.writelines('LAST_RECEIVED_TIME='+g_lastreceivedtime + '\n')
                                tmp = g_lastreceivedtime.split('-')[1].split(':')
                                lbcd = int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])
                                smsg = now + ":Quote Date not received from " + g_lastreceivedtime +"\n"
                        elif g_firstruntime != None:
                                tmp = g_firstruntime.split('-')[1].split(':')
                                lbcd = int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])
                                smsg = now + ":Quote Date not received from " + g_firstruntime +"\n"
                        if lbcd != None and (cbcd-lbcd) > 600:
                                writelog(smsg)
        pf.close()
except Exception as e:
    print str(e)
    print traceback.print_exc()
    print datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S") + " Exception catched!"
    fl.close()
    os.remove(g_processlockfile)
else:
    #print "Success!"
    fl.close()
    os.remove(g_processlockfile)
finally:
    sys.exit()