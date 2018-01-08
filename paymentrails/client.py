
import time
import hmac
import hashlib
import json
import requests

import paymentrails.exceptions.invalidServerConnectionException
import paymentrails.exceptions.unexpectedException
import paymentrails.exceptions.notFoundException
import paymentrails.exceptions.authenticationException
import paymentrails.exceptions.authorizationException
import paymentrails.exceptions.invalidFieldException
import paymentrails.exceptions.tooManyRequestsException
import paymentrails.exceptions.downForMaintenanceException
import paymentrails.exceptions.malformedException
import paymentrails.exceptions.invalidStatusException


class Client(object):
    """
    A class that makes Client requests to the API.
    """

    def __init__(self, config):
        self.config = config

    @staticmethod
    def create(config):
        """
        Factory create method
        """
        return Client(config)

    def get(self, endpoint):
        """
        Makes an HTTP GET request to the API
        """
        try:
            timestamp = int(time.time())
            authorization = self.generate_authorization(
                timestamp, "GET", endpoint, self.config)

            headers = {'Content-Type': 'application/json',
                       'Authorization': authorization,
                       'X-PR-Timestamp': str(timestamp)}

            request = requests.get(
                self.config.enviroment + endpoint, headers=headers)
            if request.status_code != 200 and request.status_code != 204:
                self.throw_status_code_exception(
                    request.status_code, request.content.decode("utf-8"))

            data = json.loads(request.content.decode("utf-8"))
            return data

        except requests.exceptions.RequestException:
            raise paymentrails.exceptions.invalidServerConnectionException.InvalidServerConnectionException(
                "Invalid Connection to the server")

    def post(self, endpoint, body):
        """
        Makes an HTTP POST request to the API
        """
        try:
            timestamp = int(time.time())
            authorization = self.generate_authorization(
                timestamp, "POST", endpoint, self.config, body)

            headers = {'Content-Type': 'application/json',
                       'Authorization': authorization,
                       'X-PR-Timestamp': str(timestamp)}

            request = requests.post(self.config.enviroment +
                                    endpoint, headers=headers, json=body)
            if request.status_code != 200 and request.status_code != 204:
                self.throw_status_code_exception(
                    request.status_code, request.content.decode("utf-8"))
            data = json.loads(request.content.decode("utf-8"))
            return data

        except requests.exceptions.RequestException:
            raise paymentrails.exceptions.invalidServerConnectionException.InvalidServerConnectionException(
                "Invalid Connection to the server")

    def patch(self, endpoint, body):
        """
        Makes an HTTP PATCH request to the API
        """
        try:

            timestamp = int(time.time())

            authorization = self.generate_authorization(
                timestamp, "PATCH", endpoint, self.config, body)

            headers = {'Content-Type': 'application/json',
                       'Authorization': authorization,
                       'X-PR-Timestamp': str(timestamp)}

            request = requests.patch(self.config.enviroment + endpoint,
                                     headers=headers, json=body)
            if request.status_code != 200 and request.status_code != 204:
                self.throw_status_code_exception(
                    request.status_code, request.content.decode("utf-8"))
            data = json.loads(request.content.decode("utf-8"))
            return data

        except requests.exceptions.RequestException:
            raise paymentrails.exceptions.invalidServerConnectionException.InvalidServerConnectionException(
                "Invalid Connection to the server")

    def delete(self, endpoint):
        """
        Makes an HTTP DELETE request to the API
        """
        try:

            timestamp = int(time.time())

            authorization = self.generate_authorization(
                timestamp, "DELETE", endpoint, self.config)

            headers = {'Content-Type': 'application/json',
                       'Authorization': authorization,
                       'X-PR-Timestamp': str(timestamp)}
            request = requests.delete(
                self.config.enviroment + endpoint, headers=headers)
            if request.status_code != 200 and request.status_code != 204:
                self.throw_status_code_exception(
                    request.status_code, request.content.decode("utf-8"))

            data = json.loads(request.content.decode("utf-8"))
            return data
        except requests.exceptions.RequestException:
            raise paymentrails.exceptions.invalidServerConnectionException.InvalidServerConnectionException(
                "Invalid Connection to the server")

    @staticmethod
    def generate_authorization(timestamp, method, endpoint, config, body=''):
        """
        Generates an authorization signature for the request header
        """
        if body != '':
            body = json.dumps(body)
        message = str(timestamp) + '\n' + method + \
            '\n' + endpoint + '\n' + body + '\n'
        key = bytes(config.get_private_key().encode('utf-8'))
        signature = hmac.new(key, msg=message.encode(
            'utf-8'), digestmod=hashlib.sha256).hexdigest()
        return 'prsign ' + config.get_public_key() + ':' + signature

    @staticmethod
    def throw_status_code_exception(status_code, message):
        """
        Throws an exception based on the type of error
        """
        if status_code == 400:
            raise paymentrails.exceptions.malformedException.MalformedException(
                message)
        elif status_code == 401:
            raise paymentrails.exceptions.authenticationException.AuthenticationException(
                message)
        elif status_code == 403:
            raise paymentrails.exceptions.authorizationException.AuthorizationException(
                message)
        elif status_code == 404:
            raise paymentrails.exceptions.notFoundException.NotFoundException(
                message)
        elif status_code == 406:
            raise paymentrails.exceptions.invalidStatusException.InvalidStatusException(
                message)
        elif status_code == 429:
            raise paymentrails.exceptions.tooManyRequestsException.TooManyRequestsException(
                message)
        elif status_code == 500:
            raise paymentrails.exceptions.invalidServerConnectionException.InvalidServerConnectionException(
                message)
        elif status_code == 503:
            raise paymentrails.exceptions.downForMaintenanceException.DownForMaintenanceException(
                message)
        else:
            raise paymentrails.exceptions.unexpectedException.UnexpectedException(
                'Unexpected HTTP_RESPONSE # ' + str(status_code))
