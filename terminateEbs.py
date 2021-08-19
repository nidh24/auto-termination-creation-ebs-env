"""
Module that terminates an EBS environment
"""
from config import Config
from ebsHandler import EBShandler
from datetime import datetime


def terminateEnv():
    print("Terminating Environment...")
    ebs = EBShandler()
    for envId in Config.envIds:
        responseEnv = ebs.terminateEnvironment(envId)
        if responseEnv:
            print("Terminating environment at ", datetime.now().strftime("%H:%M:%S %d-%m-%Y"), "\nResponse : ", responseEnv)
        else:
            print("Termination of environment failed at ", datetime.now().strftime("%H:%M:%S %d-%m-%Y"), "\nResponse : ", responseEnv)

    # responseApp = ebs.deleteApplication()
    # print(responseApp)
