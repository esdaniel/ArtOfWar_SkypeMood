#!/usr/bin/python3

"""
Script to change Skype mood status, usage: skype_mood.py new_mood

@author: Joshua Arrington
@source: https://blog.arrington.me/2012/change-your-skype-mood-text-in-linux-with-python/
"""
 
import dbus
import sys
 
def mood(text=""):
    bus = dbus.SessionBus()
    try:
        proxy = bus.get_object('com.Skype.API', '/com/Skype')
        proxy.Invoke('NAME skype_mood.py')
        proxy.Invoke('PROTOCOL 2')
        if text=="":
            command = 'GET PROFILE MOOD_TEXT'
        else:
            command = 'SET PROFILE MOOD_TEXT %s' % text
        return proxy.Invoke(command)
    except:
            print ("Could not contact Skype client")
 
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        mood(sys.argv[1])
    else:
        print (mood())