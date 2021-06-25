import urllib.parse


class UrlUtils:
    @staticmethod
    def __to_came_case(string):
        # https://stackoverflow.com/a/19053800/6626193
        components = string.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    @staticmethod
    def parse(attributes):
        params = []
        for key in attributes.keys():
            if key == "self":
                continue
            if attributes[key] is not None:
                param = UrlUtils.__to_came_case(key) + "=" + urllib.parse.quote(str(attributes[key]))
                params.append(param)

        return "&".join(params)
