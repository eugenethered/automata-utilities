import json


def as_json(data):
    return json.loads(data)


def as_pretty_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True)


def as_data(data, key, default=None):
    if key in data:
        return data[key]
    return default
