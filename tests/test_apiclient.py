#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for Boundary Annotation API Client."""


import datetime
import json
import StringIO
import time
import unittest

import mock

from context import boundary_annotations


class TestBoundaryAnnotation(unittest.TestCase):
    """Tests for Boundary Annotation API Client."""

    @mock.patch('urllib2.urlopen')
    def test_create_annotation(self, x):
        """Tests creating an Annotation by ensuring timestamps match."""
        timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
        annotation = {
            'type': 'example',
            'subtype': 'test',
            'start_time': timestamp,
            'tags': ['example', 'tag']
        }

        x.return_value = StringIO.StringIO(json.dumps(annotation))

        apiclient = boundary_annotations.BoundaryAnnotations('x', 'y')

        result = apiclient.create_annotation(annotation)

        # Simple test for now, ensure ts match.
        self.assertEqual(result['start_time'], timestamp)


if __name__ == '__main__':
    unittest.main()
