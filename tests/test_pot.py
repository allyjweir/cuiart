import pytest

import pot

def test_crs_checker():
    assert pot.validate_crs("GLC") == True
    assert pot.validate_crs("  gLc  ") == True
