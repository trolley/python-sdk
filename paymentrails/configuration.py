
from paymentrails.client import Client
from paymentrails.gateway import Gateway

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
    def gateway(public_key, private_key, enviroment):
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
        if enviroment == 'production':
            return 'https://api.trolley.com'
        elif enviroment == 'development':
            return  'http://api.railz.io'
        elif enviroment == 'integration':
           return  'http://api.local.dev:3000'
        return enviroment
    