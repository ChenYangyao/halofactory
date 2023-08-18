from halofactory.profile import NFWProfile, HernquistProfile, DoublePowerlawProfile
import pytest
import numpy as np

@pytest.fixture
def nfw():
    return NFWProfile(1.0e2, 10.0, verbose=True)

@pytest.fixture
def hernquist():
    return HernquistProfile(1.0e2, 10.0, verbose=True)

@pytest.fixture
def double_power_law():
    return DoublePowerlawProfile(1.0, 2.0, 3.0, 1.0e2, 10.0, verbose=True)

def test_create_nfw(nfw: NFWProfile):
    rs = nfw['rs']
    assert np.abs(rs - 10.0) < 1.0e-10
    
def test_create_hernquist(hernquist: HernquistProfile):
    rs = hernquist['rs']
    assert np.abs(rs - 10.0) < 1.0e-10
    
def test_create_double_power_law(double_power_law: DoublePowerlawProfile):
    rs = double_power_law['rs']
    assert np.abs(rs - 10.0) < 1.0e-10