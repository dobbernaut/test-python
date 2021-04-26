import json
from types import SimpleNamespace


class JSONToDictionary():

    def __new__(cls, json_string):
        return json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))
