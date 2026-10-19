from abc import ABC, abstractmethod


class Ticking(ABC):
    """
    Interface for objects that need to update on every simulation step.

    Methods
    -------

    on_update(delta_time : float) : void (probably void)
        called every simulation step, delta_time is the time in seconds since the previous step.

    """
    @abstractmethod
    def on_update(self, delta_time):
        pass
