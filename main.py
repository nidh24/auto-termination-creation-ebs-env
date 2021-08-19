"""
handler(event, context) is main function that is being called when
lambda function is invoked by the Angular or any other aws sdk
"""
from config import Config
from startProcess import processSchedule
from urllib.parse import unquote_plus
import time


def handler(event, context):
    """
    Main function which handles the application
    """
    try:
        # print(event)
        processSchedule(event["time"])
    except Exception as exc:
        resp = Config.error_json(str(exc))
        print(resp)
