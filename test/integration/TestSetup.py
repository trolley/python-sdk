import sys
import os

sys.path.append(os.path.abspath('.'))

from trolley.configuration import Configuration
from dotenv import dotenv_values

class TestSetup:

    @staticmethod
    def getClient():
        env_values = dotenv_values(".env")
        return Configuration.gateway(env_values['ACCESS_KEY'], env_values['SECRET_KEY'])