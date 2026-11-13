import pytest
import math
from FlowComponent import FlowComponent
from reservoir import Reservoir
from Ticking import Ticking
from fluid import Fluid
from pytest import approx
from Point import MultiplicityError
from pump import Pump
from Point import Point


class TestFlowComponent:
    # Unlike the other two projects, this one relies heavily on emergent behaviour, so most of the behaviour is implicit and there aren't many units to test; hence only 5 tests get 95% coverage.
    def test_colebrook_white(self):
        f = FlowComponent.Colebrook_White(12054, 0, 1)
        assert f == approx(0.02937793505)

    def test_pipe_length(self, fixture_1):
        assert fixture_1['pipe'].length == approx(math.sqrt(2))

    def test_pipe_pressure(self, fixture_1):
        assert fixture_1['startpoint'].pressure == pytest.approx(
            fixture_1['endpoint'].pressure)

    def test_steady_state(self, fixture_1):
        for i in range(1, 500):
            Ticking.tick(0.01)
        assert fixture_1['reservoir_1'].fluid_height == approx(
            fixture_1['reservoir_1'].fluid_height)

    def test_reservoir_multiplicity(self, fixture_1):
        with pytest.raises(MultiplicityError) as e:
            new_reservoir = Reservoir(
                fixture_1['startpoint'], 1, Fluid(1000, 0.001))

    def test_pump_curve(self):
        # Specs don't really matter.
        pump = Pump(1, Fluid(1, 1), [
                    Point([0, 0, 0]), Point([0, 0, 0])], 1, 10000, 2)
        assert pump.get_pump_pressure(0) == pytest.approx(10000)
        assert pump.get_pump_pressure(2) == pytest.approx(0)
