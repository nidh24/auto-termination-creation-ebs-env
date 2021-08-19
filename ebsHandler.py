"""
Module to handle Json functions related to EBS
"""
from boto3 import client, resource
from config import Config


class EBShandler:

    def __init__(self):
        self.client = client('elasticbeanstalk', region_name="us-east-1",
                             aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY)


    def terminateEnvironment(self, envId):
        return self.client.terminate_environment(
            EnvironmentId=envId,
            # EnvironmentName='someApp-env',
            TerminateResources=True
            # ForceTerminate=True|False
        )


    def rebuildEnvironment(self, envId):
        return self.client.rebuild_environment(
            EnvironmentId=envId
            # EnvironmentName='someApp-env' # wont rebuild with the env name. only with env-id
        )


    def describeApplications(self, listOfApplications=None):
        if listOfApplications is not None:
            return self.client.describe_applications(ApplicationNames=listOfApplications)
        else:
            return self.client.describe_applications()


    def describeEnvironments(self, application=None):
        if application is not None:
            return self.client.describe_environments(
                ApplicationName=application,
            )
        else:
            return self.client.describe_environments()


    def getListofApplications(self):
        return [application["ApplicationName"] for application in self.describeApplications()["Applications"]]


    def getListofEnvironments(self, application=None):
        return [environment["EnvironmentId"] for environment in self.describeEnvironments(application)["Environments"]]


    def getListofAppWiseEnvironments(self):
        return {application: [environment["EnvironmentId"] for environment in self.describeEnvironments(application)
        ["Environments"]] for application in self.describeApplications()}
