from datetime import date, datetime
import calendar
import re
class Verify(object):
    def __init__ (self, vehicle = None):
        self.vehicle = vehicle

    def  result(self):
        v = self.vehicle
        if v!=None:
            #Preprocessing of text in plate or license
            v_1 = int(re.sub(r'[A-Z,-]+', '', v.license, re.I))
            lDig = int(repr(v_1)[-1])
            date_1 = datetime.strptime(v.date, '%b %d %Y').date()
            day = calendar.day_name[date_1.weekday()]
            #Calculate of minutes with point of reference is 00:00
            t = datetime.strptime(v.time, '%H:%M')
            totalTime = t.hour*60 + t.minute
            #Conditions if vehicle should be in road or not
            if ((( totalTime > 420 and totalTime < 570 ) 
                or ( totalTime > 960 and totalTime < 1170 ))):
                if ((lDig==1 or lDig==2) and ( day=='Monday')):
                    print('Warning this vehicle is not autorized for road')
                elif ((lDig==3 or lDig==4) and ( day=='Tuesday')):
                    print('Warning this vehicle is not autorized for road')
                elif ((lDig==5 or lDig==6) and ( day=='Wednesday')):
                    print('Warning this vehicle is not autorized for road')
                elif ((lDig==7 or lDig==8) and ( day=='Thursday')):
                    print('Warning this vehicle is not autorized for road')
                elif ((lDig==9 or lDig==0) and ( day=='Friday')):
                    print('Warning this vehicle is not autorized for road')
                else:
                    print('Ok this Vehicle is Autorized for road')
        else:
            print('There is not information about of Vehicle')