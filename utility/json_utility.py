import json


def as_json(data, default='[]'):
    if data is None:
        return json.loads(default)
    if len(data) == 0:
        return json.loads(default)
    return json.loads(data)


def as_pretty_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True)


def as_data(data, key, default=None):
    if key in data:
        return data[key]
    return default
