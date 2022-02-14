"""
pyeight.constants
~~~~~~~~~~~~~~~~~~~~
Constants list
Copyright (c) 2017-2022 John Mihalic <https://github.com/mezz64>
Licensed under the MIT license.
"""

MAJOR_VERSION = 1
MINOR_VERSION = 0
SUB_MINOR_VERSION = 0
__version__ = '{}.{}.{}'.format(
    MAJOR_VERSION, MINOR_VERSION, SUB_MINOR_VERSION)

CLIENT_URL = 'https://client-api.8slp.net/v1'
APP_URL = 'https://app-api.8slp.net/v1'

DEFAULT_TIMEOUT = 240

CLIENT_HEADERS = {
    'content-type': "application/json",
    'connection': "keep-alive",
    'user-agent': "okhttp/4.9.1",
    'accept-encoding': "gzip",
    'accept': "application/json",
    'authority': "client-api.8slp.net",
    }

APP_HEADERS = {
    'content-type': "application/json",
    'connection': "keep-alive",
    'user-agent': "okhttp/4.9.1",
    'accept-encoding': "gzip",
    'accept': "application/json",
    'authority': "app-api.8slp.net",
    }