import pytest
import math
from FlowComponent import FlowComponent
from Ticking import Ticking
from pytest import approx


class TestFlowComponent:
    def test_colebrook_white(self):
        f = FlowComponent.Colebrook_White(12054, 0, 1)
        assert f == approx(0.02937793505)

    def test_pipe_length(self, example_pipe):
        assert example_pipe['pipe'].length == approx(math.sqrt(2))

    def test_pipe_pressure(self, example_pipe):
        assert example_pipe['startpoint'].pressure == pytest.approx(
            example_pipe['endpoint'].pressure)

    def test_steady_state(self, example_pipe):
        for i in range(1, 500):
            Ticking.tick(0.01)
        assert example_pipe['reservoir_1'].fluid_height == approx(
            example_pipe['reservoir_1'].fluid_height)


adsf = TestFlowComponent()
