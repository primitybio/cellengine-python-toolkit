import attr
import numpy
from cellengine import _helpers
from ._helpers import convert_dict

# from cellengine import Population
import importlib
from abc import ABC, abstractmethod
import munch
from .Gates import *

from .Gates.gate_util import common_gate_create


@attr.s(repr=False)
class Gate(ABC):
    """Basic abstract class for gates"""

    _posted = attr.ib(default=False)

    _properties = attr.ib(default=None)

    _population = attr.ib(default=None)

    def __repr__(self):
        return "{}(_id={}, name={})".format(self.type, self._id, self.name)

    @classmethod
    def create(cls, gates):
        """Build a Gate object from a dict of properties."""
        if type(gates) is list:
            return cls._create_multiple_gates(gates)
        else:
            return cls._create_gate(gates)

    @classmethod
    def _create_gate(cls, gate):
        """Get the gate type and return instance of the correct subclass."""
        module = importlib.import_module(__name__)
        gate_type = getattr(module, gate["type"])
        return gate_type(properties=gate)

    @classmethod
    def _create_multiple_gates(cls, gates: list):
        """Create an array of gates.
        Cellengine does not accept createPopulation when an array of gates is created
        """
        experiment_id = gates[0]["experimentId"]
        try:
            assert all([gate["experimentId"] == experiment_id for gate in gates])
        except ValueError:
            print("All gates must be posted to the same experiment")
        res = cls._post_gate(gates, experiment_id, create_population=False)
        return res
        # return [cls._create_gate(gate) for gate in res]

    @classmethod
    def _post_gate(cls, gate, experiment_id, create_population):
        """Post the gate, passing the factory as the class, which returns the correct subclass."""
        res = _helpers.base_create(
            "experiments/{}/gates".format(experiment_id),
            json=gate,
            expected_status=201,
            params={"createPopulation": create_population},
            classname=Gate,
        )
        return res

    def post(self):
        """Post a gate and update properties."""
        res = self._post_gate(
            self._properties, experiment_id=self.experiment_id, create_population=True
        )
        self._posted = True
        self._properties = res._properties

    _id = _helpers.GetSet("_id", read_only=True)

    name = _helpers.GetSet("name")

    type = _helpers.GetSet("type", read_only=True)

    experiment_id = _helpers.GetSet("experimentId", read_only=True)

    gid = _helpers.GetSet("gid")

    x_channel = _helpers.GetSet("xChannel")

    y_channel = _helpers.GetSet("yChannel")

    tailored_per_file = _helpers.GetSet("tailoredPerFile")

    fcs_file_id = _helpers.GetSet("fcsFileId")

    parent_population_id = _helpers.GetSet("parentPopulationId")

    names = _helpers.GetSet("names")

    # TODO: create_population()

    # @property
    # def population(self):
    #     """If the gate is associated with a population, it can be accessed here."""
    #     if self._population is not None:
    #         return Population(self._population)

    @property
    def model(self):
        """Return an attribute-style dict of the model.

        NOTE: This approach does allow users to change the model properties to
        invalid values (i.e. 'rectangle' to a str from a dict). We could
        prevent this by making Gate.model return a __slot__ class "Model", where each
        attr of Model was built dynamically. I wrote it this way at first, but
        couldn't figure out a way to write both get and set attribute-style accessors
        for the class. Munch does this really nicely.

        As it is, this relies on the API to validate the model
        """
        model = self._properties["model"]
        if type(model) is not Gate._Munch:
            self._properties["model"] = munch.munchify(model, factory=self._Munch)
        return model

    @model.setter
    def model(self, val):
        model = self._properties["model"]
        model.update(val)

    class _Munch(munch.Munch):
        """Extend the Munch class for a dict-like __repr__"""

    def __repr__(self):
        return "{0}".format(dict.__repr__(self))

    def _body(self, type: str, model: dict):
        body = {
            "experimentId": self.experiment_id,
            "name": self.name,
            "type": type,
            "gid": self.gid,
            "xChannel": self.x_channel,
            "yChannel": self.y_channel,
            "parentPopulationId": self.parent_population_id,
            "model": model,
        }
        return body


class RectangleGate(Gate):
    """Basic concrete class for polygon gates"""

    pass


class PolygonGate(Gate):
    """Basic concrete class for polygon gates"""

    pass

    # @property
    # def model
