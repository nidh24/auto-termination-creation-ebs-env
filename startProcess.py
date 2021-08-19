"""
startprocess function to start deleting or creating EBS env as per the cron-hour
"""
from config import Config
from createEbs import createEnv
from terminateEbs import terminateEnv
from describeEbs import describeEnv


from datetime import datetime, timedelta


def convertToIst(cronDateTime):
    return (cronDateTime + timedelta(hours=5, minutes=30)).time()


def processSchedule(cronDateTime):

    crontime_ist = convertToIst(datetime.strptime(cronDateTime, "%Y-%m-%dT%H:%M:%SZ"))
    print(crontime_ist)
    if crontime_ist == Config.createTime:
        createEnv()
    elif crontime_ist == Config.terminateTime:
        terminateEnv()
    elif crontime_ist == Config.describeTime:
        describeEnv()

