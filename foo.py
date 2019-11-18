import attr
from abc import ABC, abstractmethod


@attr.s
class GateFormatter(ABC):

    _type = attr.ib()
    experiment_id = attr.ib()
    x_channel = attr.ib()
    y_channel = attr.ib()
    name = attr.ib()
    label = attr.ib()
    gid = attr.ib()
    locked = attr.ib()
    parent_population_id = attr.ib()
    parent_population = attr.ib()
    tailored_per_file = attr.ib()
    fcs_file_id = attr.ib()
    fcs_file = attr.ib()
    create_population = attr.ib()

    @classmethod
    def create(cls, _type):
        """Instantiate a gate """
        return cls.create_gate(_type)

    @classmethod
    def create_gate(cls, _type):
        module = __import__(__name__)
        gate_class = getattr(module, _type)
        return gate_class(type=gate_class.__name__)

    @classmethod
    def create_multiple(cls, gates):
        return [cls.create_gate(gate) for gate in gates]

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    def body(self):
        body = {
            "experimentId": self.experiment_id,
            "name": self.name,
            "type": self.type,
            "gid": self.gid,
            "xChannel": self.x_channel,
            "yChannel": self.y_channel,
            "parentPopulationId": self.parent_population_id,
            "model": self.model,
        }


@attr.s
class PolygonGate(GateFormatter):
    """Basic concrete class for polygon gates"""

    x_vertices = attr.ib()
    y_vertices = attr.ib()

    @property
    def model(self):
        model = {
            "locked": False,
            "label": "none for now",
            "polygon": {
                "vertices": [[a, b] for (a, b) in zip(self.x_vertices, self.y_vertices)]
            },
        }
        return model


@attr.s
class RectangleGate(GateFormatter):
    """Basic concrete class for polygon gates"""

    x1 = attr.ib()
    x2 = attr.ib()
    y1 = attr.ib()
    y2 = attr.ib()
    label = attr.ib()

    @property
    def model(self):
        model = {
            "locked": self.locked,
            "label": self.label,
            "rectangle": {"x1": self.x1, "x2": self.x2, "y1": self.y1, "y2": self.y2},
        }
        return model
