"""
Config class
"""
from datetime import time


class Config:

    createTime = time(10, 0)
    terminateTime = time(22, 0)
    describeTime = time(16, 0)

    envIds = ["e-hszam2j2dh"]
    appIds = ["testingAutomation"] 
    
    EVENT_PAYLOAD_CREATE = {
          "version": "0",
          "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
          "detail-type": "Scheduled Event",
          "source": "aws.events",
          "account": "<account-id>",
          "time": "2021-07-29T04:30:00Z",
          "region": "us-east-1",
          "resources": [
            "arn:aws:events:us-east-1:<account-id>:rule/<event-rule-name>"
          ],
          "detail": {}
        }

    EVENT_PAYLOAD_TERMINATE = {
        "version": "0",
        "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
        "detail-type": "Scheduled Event",
        "source": "aws.events",
        "account": "<account-id>",
        "time": "2021-07-29T16:30:00Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:events:us-east-1:<account-id>:rule/<event-rule-name>"
        ],
        "detail": {}
    }

    EVENT_PAYLOAD_DESCRIBE = {
          "version": "0",
          "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
          "detail-type": "Scheduled Event",
          "source": "aws.events",
          "account": "<account-id>",
          "time": "2021-07-29T10:30:00Z",
          "region": "us-east-1",
          "resources": [
            "arn:aws:events:us-east-1:<account-id>:rule/<event-rule-name>"
          ],
          "detail": {}
        }

    @staticmethod
    def success_json(data, mess):
        return {"data": data, "status": 200,
                "msg": mess}

    @staticmethod
    def error_json(mess):
        return {"data": {}, "status": 400,
                "err_msg": mess}
