#!/usr/bin/env python
"""Boundary Annotations API Client for Python.

See also: https://app.boundary.com/docs/annotations
"""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'


import base64
import json
import urllib2


API_URL = 'https://api.boundary.com'


class BoundaryAnnotations(object):
    """Boundary Annotations API Client"""

    def __init__(self, organization_id, api_key):
        self.url = '/'.join([API_URL, organization_id, 'annotations'])

        # 'Python urllib2 Basic Auth Problem': http://bit.ly/KZDZNk
        b64_auth = base64.encodestring(
            ':'.join([api_key, ''])).replace('\n', '')
        self.auth_header = ' '.join(['Basic', b64_auth])

    def create_annotation(self, annotation):
        """Creates an Annotation in Boundary.

        @param annotation: Annotation Params per
            https://app.boundary.com/docs/annotations
        @type annotation: dict

        @return: Response from Boundary.
        @rtype: dict
        """
        annotation_json = json.dumps(annotation)
        req = urllib2.Request(
            self.url, annotation_json, {'Content-type': 'application/json'})
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', self.auth_header)
        # TODO(gba) Add error checking, since there basically isn't any.
        response = urllib2.urlopen(req)
        return json.load(response)
