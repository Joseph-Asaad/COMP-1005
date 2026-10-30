from Pipe import Pipe
from Point import Point
from abc import ABC, abstractmethod


class Gauge(metaclass=ABC):

    def __init__(self, ends):
        self.midpoint = Point([ends[0].coords[0]+0.5*(ends[1].coords[0]-ends[0].coords[0]),
                               ends[0].coords[1]+0.5 *
                               (ends[1].coords[1]-ends[0].coords[1]),
                               ends[0].coords[2]+0.5 *
                               (ends[1].coords[2]-ends[0].coords[2])
                               ])
        self.pipe_1 = Pipe(ends[0], self.midpoint)
        self.pipe_2 = Pipe(ends[1], self.midpoint)
        pass

    @abstractmethod
    def readout():
        pass
