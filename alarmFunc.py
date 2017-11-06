#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Onlyalarm.py
#  
#  Copyright 2016 Programming machine2 <chris@ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import print_function
import sys
from time import sleep 
import datetime
import energenie_on


def run(events, timer):
    pause = 30
    print ("The Upcoming Events are :")
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    while timer > 0:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if 'Alarm' in event['summary']:
                #print(start, event['summary'])
                alarmtime = event['start'].get('dateTime')
                #print ("The next alarm is at : ", alarmtime)
                now = datetime.datetime.now().isoformat() + '+01:00' # 'Z' indicates UTC time
                if alarmtime[0:16] == now[0:16]:
                    print ("The times matched")
                    energenie_on.run_func()
                    sleep(pause)
                    return 0
                #else :
                        
        #print ("time left to renewing the events is:", timer)
        sleep(pause)
        timer = timer - pause

    #print ("Trying to find new occurences of the events")            
    return 0

if __name__ == '__main__':
   
   run(sys.argv)
