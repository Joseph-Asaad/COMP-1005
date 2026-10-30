from abc import ABC, abstractmethod


class Ticking(ABC):
    """
    Interface for objects that need to update on every simulation step.

    Methods
    -------

    on_update(delta_time : float) : void (probably void)
        called every simulation step, delta_time is the time in seconds since the previous step.

    """

    ticking_objects = []
    ticking_classes = []

    def __init__(self):
        Ticking.ticking_objects.append(self)

    def TickingClass(clazz):
        Ticking.ticking_classes.append(clazz)
        return clazz

    def tick(delta_time):
        for obj in Ticking.ticking_objects:
            obj.on_update(delta_time)
        for clazz in Ticking.ticking_classes:
            clazz.on_update(delta_time)

    @abstractmethod
    def on_update(self, delta_time):
        pass
