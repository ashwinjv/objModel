import pytest

from .vector import Vector


@pytest.fixture
def wind_vector():
    return Vector([3, 4])


def test_get_u(wind_vector):
    assert wind_vector.u == 3, \
        'should have an attribute of u, equal to 2'

def test_get_v(wind_vector):
    assert wind_vector.v == 4, \
        'should have an attribute of v, equal to 3'

def test_angle(wind_vector):
    assert round(wind_vector.angle, 4) == 0.9273, \
        'should calculate angle of the vector'
        
def test_length_of_vector(wind_vector):
    assert len(wind_vector) == 2, 'length of the wind_vector should be 2'

def test_str_of_vector(wind_vector):
    assert str(wind_vector) == '(3, 4)', \
        'should have required string representation'

def test_repr_of_vector(wind_vector):
    assert repr(wind_vector) == 'Vector object: (3, 4)', \
        'should have required repr representation'

def test_iterator(wind_vector):
    assert [i for i in wind_vector] == [3, 4], \
        'should iterate to provide components'

def test_equals(wind_vector):
    assert wind_vector == Vector([3, 4]), \
        'should be equal'

def test_equals_with_different_lengths(wind_vector):
    assert wind_vector != Vector([3, 4, 5]), \
        'should not be equal when the lengths are differnet'

def test_add(wind_vector):
    assert wind_vector + Vector([3, 2]) == Vector([6, 6]), \
        'should add (3, 4) and (3, 2) to equal (6, 6)'

def test_add_with_different_lengths(wind_vector):
    with pytest.raises(TypeError):
        wind_vector + Vector([3, 2, 5])

def test_sub(wind_vector):
    assert wind_vector - Vector([3, 2]) == Vector([0, 2]), \
        'should sub (3, 4) and (3, 2) to equal (0, 2)'

def test_sub_with_different_lengths(wind_vector):
    with pytest.raises(TypeError):
        wind_vector - Vector([3, 2, 5])

def test_mul(wind_vector):
    assert wind_vector * 2 == Vector([6, 8]), \
        'should multiply all components with 2'

def test_rmul(wind_vector):
    assert 2 * wind_vector == Vector([6, 8]), \
        'should multiply all components with 2'

def test_abs(wind_vector):
    assert abs(wind_vector) == 5, \
        'should be equal to 5'

def test_getitems_by_index(wind_vector):
    assert wind_vector[0] == 3, \
        'should get items by index'

def test_get_by_name(wind_vector):
    assert wind_vector['u'] == 3, \
        'should get items by key' 
        