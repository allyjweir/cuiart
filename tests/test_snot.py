#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_snot
----------------------------------

Tests for `snot` module. (Previously `snakes_on_a_train`)
"""

import pytest
import os

from contextlib import contextmanager

import snot


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_initialise_api():
    foo = snot.NationalRailAPI(os.environ["NR_API_KEY"])
    assert True

def test_get_next_trains():
    foo = snot.NationalRailAPI(os.environ["NR_API_KEY"])
    result = foo.get_next_trains("GLC", "PYG")
    assert result["from_crs"] == "GLC"
    assert result["to_crs"] == "PYG"
