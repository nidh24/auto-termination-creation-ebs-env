"""
Module that describes EBS environment
"""
from config import Config
from ebsHandler import EBShandler
from datetime import datetime


def describeEnv():
    print("Describing Environments...")
    ebs = EBShandler()

    print("getting a List of Applications : ", ebs.getListofApplications())
    for appId in Config.appIds:
        print("getting a List of Environments in an application : ", appId, " \n" ,ebs.getListofEnvironments(appId))
    print("getting a List of Environments application wise : ", ebs.getListofAppWiseEnvironments())

