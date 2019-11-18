import attr

import importlib
from abc import ABC, abstractmethod
from . import _helpers


@attr.s(repr=False)
class Gate(ABC):
    """Basic abstract class for gates"""

    experiment_id = attr.ib(default=None)
    id = attr.ib(default=None)
    name = attr.ib(default=None)
    type = attr.ib(default=None)
    gid = attr.ib(default=None)
    x_channel = attr.ib(default=None)
    y_channel = attr.ib(default=None)
    parent_population_id = attr.ib(default=None)
    model = attr.ib(default=None)
    label = attr.ib(default=None)
    locked = attr.ib(default=None)
    fcs_file_id = attr.ib(default=None)
    tailored_per_file = attr.ib(default=False)
    names = attr.ib(default=[])

    @classmethod
    def create(cls, gate):
        """Get the gate type and return instance of the correct subclass."""
        module = importlib.import_module(__name__)
        if type(gate) is dict or type(gate) is list:
            gate_type = getattr(module, gate["type"])
            return gate_type(cls.deserialize_gate(gate))
        else:
            gate_type = getattr(module,)
            return gate_type()

    @staticmethod
    def deserialize_gate(dict_values):
        dict_values = _helpers.convert_dict(dict_values, "camel_to_snake")
        dict_values["id"] = dict_values.pop("_id")
        result = Gate.create(**dict_values)
        return result


@attr.s(repr=False)
class PolygonGate(Gate):
    """Basic concrete class for polygon gates"""

    pass

    # def __init__(self):
    #     self.type = "PolygonGate"

    # @property
    # def model(self):
    #     model = {
    #         "polygon": {"vertices": [[a, b] for (a, b) in zip(x_vertices, y_vertices)]},
    #     }

    #     body = {
    #         "experimentId": experiment_id,
    #         "name": name,
    #         "type": "PolygonGate",
    #         "gid": gid,
    #         "xChannel": x_channel,
    #         "yChannel": y_channel,
    #         "parentPopulationId": parent_population_id,
    #         "model": model,
    #     }
