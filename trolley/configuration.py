
from trolley.client import Client
from trolley.gateway import Gateway
from dotenv import dotenv_values

class Configuration(object):
    """
    Configuration registry
    """

    public_key = ''
    private_key = ''
    enviroment = ''

    def __init__(self, public_key="", private_key="", enviroment=""):
        self.public_key = public_key
        self.private_key = private_key
        self.enviroment = Configuration.set_enviroment(enviroment)

    @staticmethod
    def gateway(public_key, private_key, enviroment = 'production'):
        return Gateway(Configuration(public_key, private_key, enviroment))

    @staticmethod
    def client(config):
        return Client.create(config)

    @staticmethod
    def instantiate():
        return Configuration()

    @staticmethod
    def set_public_key(public_key):
        """
        Set method for the public key
        """
        Configuration.public_key = public_key

    @staticmethod
    def get_public_key():
        """
        Get method for the public key
        """
        return Configuration.public_key

    @staticmethod
    def get_private_key():
        """
        Get method for the private key
        """
        return Configuration.private_key

    @staticmethod
    def set_private_key(private_key):
        """
        Get method for the private key
        """
        Configuration.private_key = private_key
    @staticmethod
    def set_api_base(enviroment):
        Configuration.enviroment = Configuration.set_enviroment(enviroment)

    @staticmethod
    def set_enviroment(enviroment):
        """
        Set method to change the enviroment
        """
        if enviroment == 'development':
            env_values = dotenv_values(".env")

            if len(env_values['SERVER_URL']) == 0:
                raise Exception("Environment selected is 'development' but SERVER_URL is empty in .env")
            else:
                return  env_values['SERVER_URL']
        
        return 'https://api.trolley.com'
    