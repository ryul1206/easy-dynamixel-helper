#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def byteify(unicode_json):
    """Correct data type of JSON to python data.

    Thanks to Mark Amery from StackOverflow.
    https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json
    """
    # Python 2.x
    if sys.version_info[0] < 3:
        if isinstance(unicode_json, dict):
            return {byteify(key): byteify(value) for key, value
                in unicode_json.iteritems()}
        elif isinstance(unicode_json, list):
            return [byteify(element) for element in unicode_json]
        elif isinstance(unicode_json, unicode):
            return unicode_json.encode('utf-8')
        return unicode_json
    # Python 3.x
    else:
        if isinstance(unicode_json, dict):
            return {byteify(key): byteify(value) for key, value
                in unicode_json.items()}
        elif isinstance(unicode_json, list):
            return [byteify(element) for element in unicode_json]
        return unicode_json
