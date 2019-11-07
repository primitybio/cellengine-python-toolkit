import importlib
from abc import ABC, abstractmethod


class Gate(ABC):
    """Basic abstract class for gates"""

    def __init__(self, gate_class=None, name=None, _id="none"):
        self.gate_class = gate_class
        self._id = _id
        self.name = name

    def __repr__(self):
        return "{}(name={}, _id={})".format(self.gate_class, self.name, self._id)

    @classmethod
    def create(cls, gates):
        """Instantiate a gate """
        if type(gates) is list:
            return cls.create_multiple(gates)
        else:
            return cls.create_gate(gates)

    @classmethod
    def create_gate(cls, gate):
        module = importlib.import_module(__name__)
        print(module)
        gate_class = getattr(module, gate)
        return gate_class(gate_class=gate_class.__name__)

    @classmethod
    def create_multiple(cls, gates):
        return [cls.create_gate(gate) for gate in gates]

    @property
    @abstractmethod
    def model(self):
        pass


class PolygonGate(Gate):
    """Basic concrete class for polygon gates"""

    @property
    def model(self):
        model = {
            "locked": False,
            "label": "none for now",
            "polygon": {"vertices": "some vertices here"},
        }
        return model
