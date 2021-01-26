from datetime import datetime
import pytz

def ist():
    return pytz.timezone("Asia/Kolkata")

def dt_now():
    return datetime.now(ist()).strftime("%Y-%m-%d %H:%M:%S")