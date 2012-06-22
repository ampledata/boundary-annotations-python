Boundary Annotations API Client for Python.


Installation
============

::
    pip install boundary_annotations


Usage Example
=============

::
    import boundary_annotations
    
    
    annotation = {
        'type': 'example',
        'subtype': 'test'
    }
    
    apiclient = boundary_annotations.BoundaryAnnotations('a', 'b')
    
    apiclient.create_annotation(annotation)


More Information
================
Please see the Boundary Annotations API Documentation https://app.boundary.com/docs/annotations


Source
======
https://github.com/ampledata/boundary-annotations-python

Author
======
Greg Albrecht mailto:gba@splunk.com


Copyright
=========
Copyright 2012 Splunk, Inc.


License
=======
Apache License 2.0
