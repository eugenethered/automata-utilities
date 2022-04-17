import os
import requests


SETUP_CFG_FILE = f'{os.getcwd()}/setup.cfg'
RELEASE_INFO_URL = 'https://pypi.org/pypi/persuader.technology.automata.utilities/json'


def read_from_file(file_path):
    with open(file_path, 'r') as data_file:
        return data_file.readlines()


def get_current_version():
    file_contents = read_from_file(SETUP_CFG_FILE)
    version = [line for line in file_contents if line.find('version') >= 0]
    normalized_version = version[0].replace('\n', '').replace(' ', '').replace('version=', '')
    return normalized_version


def get_released_version():
    response = requests.get(RELEASE_INFO_URL)
    if response.status_code == requests.codes.ok:
        json_payload = response.json()
        latest_released_version = json_payload['info']['version']
        return latest_released_version


def normalize_version(version):
    if version is None:
        return 0
    return int(version.replace('.', ''))


if __name__ == '__main__':
    current_version = get_current_version()
    released_version = get_released_version()
    if normalize_version(current_version) > normalize_version(released_version):
        print('RELEASE_TO_PIPY=true')
    else:
        print('RELEASE_TO_PIPY=false')
