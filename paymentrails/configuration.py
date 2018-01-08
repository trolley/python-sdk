
from paymentrails.client import Client
# import paymentrails.client
from paymentrails.gateway import Gateway

class Configuration(object):
    """
    Configuration registry
    """

    public_key = ''
    private_key = ''
    enviroment = 'https://api.paymentrails.com'

    @staticmethod
    def gateway():
        return Gateway(config=Configuration.instantiate())

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
    def set_enviroment(enviroment):
        """
        Set method to change the enviroment
        """
        if enviroment == 'production':
            Configuration.enviroment = 'https://api.paymentrails.com'
        elif enviroment == 'development':
            Configuration.enviroment = 'http://api.railz.io'
        elif enviroment == 'integration':
            Configuration.enviroment = 'http://api.local.dev:3000'
