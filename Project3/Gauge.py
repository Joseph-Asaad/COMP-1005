from Pipe import Pipe
from Point import Point
from abc import ABC, abstractmethod


class Gauge(ABC):

    def __init__(self, radius, fluid, ends, roughness, length=None):
        self.midpoint = Point([ends[0].coords[0]+0.5*(ends[1].coords[0]-ends[0].coords[0]),
                               ends[0].coords[1]+0.5 *
                               (ends[1].coords[1]-ends[0].coords[1]),
                               ends[0].coords[2]+0.5 *
                               (ends[1].coords[2]-ends[0].coords[2])
                               ])
        if not length == None:
            length = length/2

        self.pipe_1 = Pipe(
            radius, fluid, [ends[0], self.midpoint], roughness, length)
        self.pipe_2 = Pipe(
            radius, fluid, [ends[1], self.midpoint], roughness, length)

    @abstractmethod
    def readout(self):
        pass
