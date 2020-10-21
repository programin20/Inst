import datetime
from datetime import timedelta
import time
import os 
TimeNow = datetime.datetime.now()
LastTime = datetime.datetime.now()
while True:
    if TimeNow.hour!=LastTime.hour:
        myCmd = '%SystemRoot%\\system32\\rundll32.exe USER32.DLL LockWorkStation'
        os.system (myCmd)
        TimeNow = datetime.datetime.now()
    time.sleep(60)
    LastTime = datetime.datetime.now()
