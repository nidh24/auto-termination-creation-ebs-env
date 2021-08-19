"""
Module that creates an EBS environment
"""
from config import Config
from ebsHandler import EBShandler
from datetime import datetime


def createEnv():
    print("Re-building Environment...")
    ebs = EBShandler()
    # responseApp = ebs.createApplication()
    # print(responseApp)

    # check_dns_availability()  ## can check dns_availability
    # print(ebs.client.list_available_solution_stacks())

    # responseEnv = ebs.createEnvironment()
    # print(responseEnv)
    for envId in Config.envIds:

        responseRebuild = ebs.rebuildEnvironment(envId)
        if responseRebuild:
            print("Re-building environment at ", datetime.now().strftime("%H:%M:%S %d-%m-%Y"), "\nResponse : ", responseRebuild)
        else:
            print("Re-building of environment failed at ", datetime.now().strftime("%H:%M:%S %d-%m-%Y"), "\nResponse : ", responseRebuild)
