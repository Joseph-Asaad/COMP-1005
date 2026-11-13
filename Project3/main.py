from Ticking import Ticking
from FlowComponent import FlowComponent
from Point import Point
from reservoir import Reservoir
from fluid import Fluid
from Pipe import Pipe
from pump import Pump
import time
from multi_gauge import MultiGauge

## Simulation setup ##

TICK_RATE = 20  # In cycles/s.
TIMESCALE = 5

## Physical Setup ##

water = Fluid(1000, 0.001)

top_point = Point([0, 0, 1])
mid_point = Point([0, 0.5, 0.5])
bottom_point = Point([0, 1, 0])

top_reservoir = Reservoir(top_point, 1, water)
bottom_reservoir = Reservoir(bottom_point, 0.5, water)

# Concrete pipe betwixt the two points, starts filled with water.
# the_pipe = Pipe(0.05, water, [top_point, bottom_point], 0.0003)

the_pump = Pump(0.05, water, [top_point, mid_point], 0.0003, 10000, 1)
the_pipe = Pipe(0.05, water, [bottom_point, mid_point], 0.0003)
# multi_gauge = MultiGauge(0.05, water, [mid_point, bottom_point], 0.0003)

# Fill with 5m of water.
bottom_reservoir.fluid_height = 5
top_reservoir.fluid_height = 0

## Running ##

prev_time = time.time()
initial_time = time.time()
step_count = 0

print("\n\n\n\n\n\n\n\n\n\n\n")  # Clear output.
for i in range(1, 10000):

    print("\x1b[9F")
    # print("\n\n\n\n\n\n\n\n\n\n\n")
    print(
        f"----------- T:{step_count/TICK_RATE:.1f}, Step #{step_count} -----------")
    print(
        f"Fill height: Top: {top_reservoir.fluid_height:.2f}, Bottom: {bottom_reservoir.fluid_height:.2f}")
    print(
        f"Fill rate  : Top: {top_reservoir.fill_rate:.4f}, Bottom: {bottom_reservoir.fill_rate:.4f}")
    print(
        f"Volume: Top: {top_reservoir.volume:.2f}, Bottom: {bottom_reservoir.volume:.2f}")
    print(
        f"Pressure: Top: {top_point.pressure:.0f}, Bottom: {bottom_point.pressure:.0f}, Pump: {the_pump.flow_component.h_pump:.3f}")
    print(f"Pipe flow velocity: {the_pump.flow_component.velocity:.2f}")
    Ticking.tick(1/TICK_RATE)

    # Advance time according to settings.
    while time.time() - prev_time < 1/TICK_RATE/TIMESCALE:
        pass
    prev_time = time.time()
    step_count += 1

    if i == 2000:
        the_pump.throttle = 1
