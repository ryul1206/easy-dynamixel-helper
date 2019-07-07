#!/usr/bin/env python
# -*- coding: utf-8 -*-


def byteify(unicode_json):
    # Thanks to Mark Amery from StackOverflow.
    # https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json
    if isinstance(unicode_json, dict):
        return {byteify(key): byteify(value)
                for key, value in unicode_json.iteritems()}
    elif isinstance(unicode_json, list):
        return [byteify(element) for element in unicode_json]
    elif isinstance(unicode_json, unicode):
        return unicode_json.encode('utf-8')
    return unicode_json
