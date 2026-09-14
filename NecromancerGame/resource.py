from typing import Tuple


class Resource:
    """
    At
    Methods
    -------
    add_resource (resource : ResourceType  count : int) : void
        adds/subtracts from the selected resource.
    subtract_resource (resource : ResourceType  count : int) : void
            adds/subtracts from the selected resource.
    get_resource (resource : ResourceType, count : int) : int
        returns the count of the selected resource.
    """  # TODO : update
    from enum import Enum

    class ResourceTypes(Enum):
        NECROTIC = ("necrotic_runes", 0)
        SPIRIT = ("spirit_runes", 1)
        BONE = ("bone_runes", 2)
        FLESH = ("flesh_runes", 3)
        ECTOPLASM = ("ectoplasm", 4)

    def __init__(self):
        self.__resources = []  # Start with empty array.

        for typ in self.ResourceTypes:
            self.__resources.append(0)  # Initialise amount at 0.
            name = typ.value[0]  # Extract name, index from enum.
            index = typ.value[1]

            # Temporary namespace for automatically generating functions.
            namespace = {}

            exec(  # Dynamically generate a setter in the namespace dict.
                f"""def {name}_getter(self):
                return self._{self.__class__.__name__}__resources[{index}]""",
                globals(),
                namespace
            )
            setattr(self.__class__, f"{name}_getter",  # Move the function from the namespace to the class
                    namespace[f"{name}_getter"])

            exec(f"{self.__class__.__name__}.{name} = property({self.__class__.__name__}.{name}_getter, None)",  # create a property from the getter
                 globals(), namespace)

    # add_resource([])
    def add_resource(self, counts: Tuple[int, int, int, int, int]):
        if not (count >= 0 for count in counts):
            return
        self.__resources = [a + b for a,
                            b in zip(self.__resources, list(counts))]

    # add_resource([])
    def subtract_resource(self, counts: Tuple[int, int, int, int, int], simulate: bool):
        if (not count >= 0 for count in counts):
            raise (ValueError)
        if (not prev - sub >= 0 for prev, sub in zip(self.__resources, list(counts))):
            return False
        if simulate:
            for i in counts:
                self.__resources[i] -= counts[i]
        return True

    def get_resource(self, resource):
        return self.__resources[resource.value]
