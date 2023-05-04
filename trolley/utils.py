import urllib.parse


class UrlUtils:
    """
    Helper class which allows automatic conversion from Python function parameters to Payment
    Rails supported API parameters.
    """

    @staticmethod
    def __to_came_case(string):
        """
        Converts the given string from snake_case (Python PEP) to lowerCamelCase (Trolley API)
        See: https://stackoverflow.com/a/19053800/6626193

        :param string: the given snake_case string
        :return: the equivalent lowerCamelCase string
        """
        components = string.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    @staticmethod
    def parse(attributes):
        """
        Given a series of attributes in a dictionary, parses such dictionary removing all None values and
        returns a URL compatible parameter string.
        To use this method, invoke it like UrlUtils.parse(locals()), as locals() will return all parameters that
        the function is receiving.
        For an example, see RecipientGateway.search.

        :param: attributes: dictionary of all attributes, including None ones
        :return: url compatible parameter string
        """

        # List containing already parsed params [key1=value1, key2=value2]
        params = []
        # Iterate over attribute keys
        for key in attributes.keys():
            # Note that locals() also returns the "self" attribute, so just ignore it
            if key == "self":
                continue

            # Ignore None attributes as well
            if attributes[key] is None:
                continue

            # Convert the valid parameter to a Trolley API compatible one
            param = UrlUtils.__to_came_case(key) + "=" + urllib.parse.quote(str(attributes[key]))
            # And add it to the list
            params.append(param)

        # Return the list as a string with "&" as the join character
        return "&".join(params)
