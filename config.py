from dotenv import load_dotenv
import os

load_dotenv()

class teleConfig:
    API_ID = os.environ["API_ID"]
    API_HASH = os.environ["API_HASH"]
    CHANNEL_NAME = os.environ["CHANNEL_NAME"]