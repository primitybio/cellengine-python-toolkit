from cellengine import _helpers
import importlib
from abc import ABC, abstractmethod
import munch
from ..Gates import create_polygon_gate


class BaseGate(ABC):
    """Basic abstract class for gates"""

    def __init__(self, type=None, _properties=None):
        self.type = type
        self._properties = _properties

    def __repr__(self):
        return "{}(_id={}, name={})".format(self.type, self._id, self.name)

    @classmethod
    def create(cls, gates):
        """Build a gate object from a dict of properties."""
        if type(gates) is list:
            return cls.create_multiple(gates)
        else:
            return cls.create_gate(gates)

    @classmethod
    def create_gate(cls, gate):
        """Get the gate type and return instance of the correct subclass."""
        module = importlib.import_module(__name__)
        _type = getattr(module, gate["type"])
        res = cls.post_gate(gate)
        return _type(type=_type.__name__, _properties=res)

    @classmethod
    def create_multiple(cls, gates):
        return [cls.create_gate(gate) for gate in gates]

    @classmethod
    def post_gate(cls, gate):
        res = _helpers.session.post(
            f"experiments/{gate['experimentId']}/gates", json=gate
        )
        print(res.json())
        return res.json()

    @property
    @abstractmethod
    def model(self):
        pass


class Gate(BaseGate):
    """Basic concrete class for gates"""

    _id = _helpers.GetSet("_id", read_only=True)

    name = _helpers.GetSet("name")

    experiment_id = _helpers.GetSet("experimentId", read_only=True)

    gid = _helpers.GetSet("gid")

    x_channel = _helpers.GetSet("xChannel")

    y_channel = _helpers.GetSet("yChannel")

    tailored_per_file = _helpers.GetSet("tailoredPerFile")

    fcs_file_id = _helpers.GetSet("fcsFileId")

    parent_population_id = _helpers.GetSet("parentPopulationId")

    names = _helpers.GetSet("names")

    locked = _helpers.GetSet("locked")

    label = _helpers.GetSet("label")

    @property
    def model(self):
        """Return an attribute-style dict of the model.

        NOTE: This approach does allow users to change the model properties to
        invalid values (i.e. 'rectangle' to a str from a dict). We could
        prevent this by making Gate.model return a __slot__ class "Model", where each
        attr of Model was built dynamically. I wrote it this way at first, but
        couldn't figure out a way to write both get and set attribute-style accessors
        for the class. Munch does this really nicely.

        As it is, this relies on the API to validate the model. If necessary, I
        can write validators in here as well.
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


class RectangleGate(Gate):
    """Basic concrete class for polygon gates"""

    pass

    # @property
    # def model(self):
    #     model = {
    #         "locked": self.locked,
    #         "label": self.label,
    #         "rectangle": {"x1": self.x1, "x2": self.x2, "y1": self.y1, "y2": self.y2},
    #     }
    #     return model


class PolygonGate(Gate):
    """Basic concrete class for polygon gates"""

    @classmethod
    def create(
        cls,
        experiment_id,
        x_channel,
        y_channel,
        name,
        x_vertices,
        y_vertices,
        label=[],
        gid=None,
        locked=False,
        parent_population_id=None,
        parent_population=None,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
        create_population=True,
    ):
        return create_polygon_gate(
            experiment_id,
            x_channel,
            y_channel,
            name,
            x_vertices,
            y_vertices,
            label,
            gid,
            locked,
            parent_population_id,
            parent_population,
            tailored_per_file,
            fcs_file_id,
            fcs_file,
            create_population,
        )

    @property
    def model(self):
        model = {
            "locked": False,
            "label": "none for now",
            "polygon": {"vertices": "some vertices here"},
        }
        return model
