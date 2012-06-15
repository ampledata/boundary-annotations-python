#!/usr/bin/env python
"""Boundary Annotation API Client for Python.

See also: https://app.boundary.com/docs/annotations
"""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'


import base64
import datetime
import json
import urllib2
import time
import unittest


API_URL = 'https://api.boundary.com'


class BoundaryAnnotation(object):
    """Boundary Annotations API Client"""
    def __init__(self, organization_id, api_key):
        self.url = '/'.join([API_URL, organization_id, 'annotations'])

        # 'Python urllib2 Basic Auth Problem': http://bit.ly/KZDZNk
        b64_auth = base64.encodestring(
            ':'.join([api_key, ''])).replace('\n', '')
        self.auth_header = ' '.join(['Basic', b64_auth])

    def create_annotation(self, annotation):
        """Creates an Annotation in Boundary.

        TODO(gba) Add error checking, since there basically isn't any :(.

        @param annotation: Annotation Params per
            https://app.boundary.com/docs/annotations
        @type annotation: dict

        @return: Response from Boundary.
        @rtype: dict (hopefully!)
        """
        annotation_json = json.dumps(annotation)
        req = urllib2.Request(
            self.url, annotation_json, {'Content-type': 'application/json'})
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', self.auth_header)
        response = urllib2.urlopen(req)
        return json.load(response)


class TestBoundaryAnnotation(unittest.TestCase):
    """Tests for Boundary Annotation API Client."""
    def test_create_annotation(self):
        """Tests creating an Annotation by ensuring timestamps match."""
        timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
        annotation = {
            'type': 'example',
            'subtype': 'test',
            'start_time': timestamp,
            'end_time': timestamp,
            'tags': ['example', 'tag']
        }

        apiclient = BoundaryAnnotation('CUSTOMER_ID', 'API_KEY')
        result = apiclient.create_annotation(annotation)

        # Simple test for now, ensure ts match.
        self.assertEqual(result['start_time'], timestamp)


if __name__ == '__main__':
    unittest.main()
