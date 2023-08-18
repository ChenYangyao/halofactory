from .test_profile import nfw, NFWProfile, hernquist, HernquistProfile, double_power_law, DoublePowerlawProfile
from halofactory.initial_condition import Jeans, EddInv
import pytest
import numpy as np

@pytest.fixture
def jeans(nfw: NFWProfile):
    return Jeans(nfw, verbose=True)

@pytest.fixture
def edd_inv(hernquist: HernquistProfile):
    return EddInv(hernquist, verbose=True)

def test_create_jeans(jeans: Jeans):
    ps = jeans.get(1000)
    assert ps.pos.shape == (1000, 3)
    assert ps.vel.shape == (1000, 3)
    assert np.isscalar(ps.mass)
    
def test_create_edd_inv(edd_inv):
    ps = edd_inv.get(1000)
    assert ps.pos.shape == (1000, 3)
    assert ps.vel.shape == (1000, 3)
    assert np.isscalar(ps.mass)