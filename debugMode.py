"""
for testing purposes on local
"""

from main import handler
from config import Config

handler(event=Config.EVENT_PAYLOAD_CREATE, context="")
handler(event=Config.EVENT_PAYLOAD_DESCRIBE, context="")
handler(event=Config.EVENT_PAYLOAD_TERMINATE, context="")
