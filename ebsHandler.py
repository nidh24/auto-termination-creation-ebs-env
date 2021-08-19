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


    def createApplication(self):
        return self.client.create_application(
            ApplicationName='someApp',
            Description='app created using python sdk'
            # ResourceLifecycleConfig={
            #     'ServiceRole': 'string',
            #     'VersionLifecycleConfig': {
            #         'MaxCountRule': {
            #             'Enabled': True|False,
            #             'MaxCount': 123,
            #             'DeleteSourceFromS3': True|False
            #         },
            #         'MaxAgeRule': {
            #             'Enabled': True|False,
            #             'MaxAgeInDays': 123,
            #             'DeleteSourceFromS3': True|False
            #         }
            #     }
            # },
            # Tags=[
            #     {
            #         'Key': 'string',
            #         'Value': 'string'
            #     },
            # ]
        )


    def deleteApplication(self):
        return self.client.delete_application(
            ApplicationName='someApp',
            TerminateEnvByForce=True
        )


    def createEnvironment(self):
        return self.client.create_environment(
            ApplicationName='someApp',
            EnvironmentName='someApp-env',
            # GroupName='string',
            Description='Test env for test app created using SDK',
            CNAMEPrefix='someApp-env',  ## if not given, env-name is concatenated with random letters
            Tier={
                'Name': 'WebServer',
                'Type': 'Standard'
            },
            TemplateName='someApp-config'  ## need a saved configuration for deploying environment
            # SolutionStackName='64bit Amazon Linux 2 v3.3.3 running Python 3.7'  ## not working
            # PlatformArn='string',
            # Tags=[
            #     {
            #         'Key': 'string',
            #         'Value': 'string'
            #     },
            # ],
            # VersionLabel='string',
            # OptionSettings=[
            #     {
            #         'ResourceName': 'string',
            #         'Namespace': 'string',
            #         'OptionName': 'string',
            #         'Value': 'string'
            #     },
            # ],
            # OptionsToRemove=[
            #     {
            #         'ResourceName': 'string',
            #         'Namespace': 'string',
            #         'OptionName': 'string'
            #     },
            # ],
            # OperationsRole='string'
        )


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
                # VersionLabel='string',
                # EnvironmentIds=[
                #     'string',
                # ],
                # EnvironmentNames=[
                #     'string',
                # ],
                # IncludeDeleted=True | False,
                # IncludedDeletedBackTo=datetime(2015, 1, 1),
                # MaxRecords=123,
                # NextToken='string'
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
