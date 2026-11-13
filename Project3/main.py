from Ticking import Ticking
from FlowComponent import FlowComponent
from Point import Point
from reservoir import Reservoir
from fluid import Fluid
from Pipe import Pipe
import time

## Simulation Setup ##

TICK_RATE = 20  # In cycles/s.
TIMESCALE = 5  # 5x real speed.

## Physical Setup ##

water = Fluid(1000, 0.001)  # Density and viscosity of water.

# Create two points diagonally positioned.
top_point = Point([0, 0, 1])
bottom_point = Point([0, 1, 0])

# A reservoir at each point.
top_reservoir = Reservoir(top_point, 1, water)
bottom_reservoir = Reservoir(bottom_point, 0.5, water)

# Concrete pipe betwixt the two points, starts filled with water.
the_pipe = Pipe(0.05, water, [top_point, bottom_point], 0.0003)

# Fill bottom reservoir with 5m of water, or 4m above bottom of top reservoir.
# Because of this, water should flow from the bottom reservoir to the top.
bottom_reservoir.fluid_height = 5
top_reservoir.fluid_height = 0

## Running ##

prev_time = time.time()
initial_time = time.time()
step_count = 0

print("\n\n\n\n\n\n\n\n\n\n\n")  # Clear output.
for i in range(1, 1000):

    print("\x1b[7F")
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
        f"Pressure: Top: {top_point.pressure:.0f}, Bottom: {bottom_point.pressure:.0f}")
    print(f"Pipe flow velocity: {the_pipe.flow_component.velocity:.2f}")
    Ticking.tick(1/TICK_RATE)

    # Advance time according to settings.
    while time.time() - prev_time < 1/TICK_RATE/TIMESCALE:
        pass
    prev_time = time.time()
    step_count += 1
