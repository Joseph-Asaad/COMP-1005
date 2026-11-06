import pytest
import math


@pytest.fixture
def example_pipe():
    from Point import Point
    from Pipe import Pipe
    from fluid import Fluid
    from reservoir import Reservoir
    out = {}
    water = Fluid(1000, 0.001)
    out["startpoint"] = Point([0, 0, 0])
    out["endpoint"] = Point([1, 1, 0])
    out['pipe'] = Pipe(
        0.01, water, [out['startpoint'], out['endpoint']], 0.000025)
    out['reservoir_1'] = Reservoir(
        out['startpoint'], 1/math.sqrt(math.pi), water)
    out['reservoir_2'] = Reservoir(
        out['endpoint'], 1/math.sqrt(math.pi), water)
    # Fill with 5m of water.
    out['reservoir_1'].fluid_height = 2
    out['reservoir_1'].on_update(0)  # Update so changes take effect.
    out['reservoir_2'].fluid_height = 2
    out['reservoir_2'].on_update(0)  # Update so changes take effect.
    return out
