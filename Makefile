# Makefile or Boundary Annotations API Client
#
# Author:: Greg Albrecht <mailto:gba@splunk.com>
# Copyright:: Copyright 2012 Splunk, Inc.
# License:: All rights reserved. Do not redistribute.
#


init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

lint:
	pylint -i y -r n -f colorized boundary_annotations
	pylint -i y -r n -f colorized tests/*.py
	pylint -i y -r n -f colorized *.py

pep8:
	pep8 boundary_annotations/*.py
	pep8 tests/*.py
	pep8 *.py

install:
	pip install .

uninstall:
	pip uninstall boundary_annotations
