import attr
import numpy
from cellengine import _helpers

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
        # res = _helpers.base_create(
        #     url="experiments/{}/gates".format(experiment_id),
        #     json=gates,
        #     experiment_id=experiment_id,
        #     expected_status=201,
        #     create_population=False,
        # )
        res = cls._post_gate(gates, experiment_id, create_population=False)
        return [cls._create_gate(gate) for gate in res]

    @classmethod
    def _post_gate(cls, gate, experiment_id, create_population):
        res = _helpers.base_create(
            "experiments/{}/gates".format(experiment_id),
            json=gate,
            expected_status=201,
            # params={"createPopulation": create_population},
        )
        return res

    def post(self):
        res = self._post_gate(
            self._properties, experiment_id=self.experiment_id, create_population=True
        )
        self._posted = True
        self._properties = res

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


class RectangleGate(Gate):
    """Basic concrete class for polygon gates"""

    pass


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

        body = format_polygon_gate(
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
        )

        return cls.create_gate(body, create_population=create_population)

        # # TODO: get population


class FormatGate:
    def model(self, gate_model: dict) -> dict:
        model = {
            "locked": locked,
            "label": label,
        }
        return model.update(gate_model)

    def body(
        self,
        experiment_id,
        type,
        name,
        gid,
        x_channel,
        y_channel,
        parent_population_id,
        model,
    ):
        body = {
            "experimentId": experiment_id,
            "name": name,
            "type": "PolygonGate",
            "gid": gid,
            "xChannel": x_channel,
            "yChannel": y_channel,
            "parentPopulationId": parent_population_id,
            "model": model,
        }
        return body

    def parse_fcs_file_args(
        self, experiment_id, body, tailored_per_file, fcs_file_id, fcs_file
    ):
        """Find the fcs file ID if 'tailored_per_file' and either 'fcs_file' or
        'fcs_file_id' are specified."""
        if fcs_file is not None and fcs_file_id is not None:
            raise ValueError("Please specify only 'fcs_file' or 'fcs_file_id'.")
        if fcs_file is not None and tailored_per_file is True:  # lookup by name
            _file = get_fcsfile(experiment_id, name=fcs_file)
            fcs_file_id = _file._id
        body["tailoredPerFile"] = tailored_per_file
        body["fcsFileId"] = fcs_file_id
        return body

    def snake_to_camel(self, body):
        body = _helpers.convert_dict(body, "snake_to_camel")
        return body

    def format_rectangle_gate(
        self,
        experiment_id,
        x_channel,
        y_channel,
        name,
        x1,
        x2,
        y1,
        y2,
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
        if label == []:
            label = [numpy.mean([x1, x2]), numpy.mean([y1, y2])]

        if gid is None:
            gid = _helpers.generate_id()

        model = self.model({"rectangle": {"x1": x1, "x2": x2, "y1": y1, "y2": y2}})

        body = {
            "experimentId": experiment_id,
            "name": name,
            "type": "RectangleGate",
            "gid": gid,
            "xChannel": x_channel,
            "yChannel": y_channel,
            "parentPopulationId": parent_population_id,
            "model": model,
        }

        return common_gate_create(
            experiment_id,
            body=body,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
            create_population=create_population,
        )

    def format_polygon_gate(
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
        if label == []:
            label = [numpy.mean(x_vertices), numpy.mean(y_vertices)]

        if gid is None:
            gid = _helpers.generate_id()

        model = {
            "locked": locked,
            "label": label,
            "polygon": {"vertices": [[a, b] for (a, b) in zip(x_vertices, y_vertices)]},
        }

        return body


def get_fcsfile(experiment_id, _id=None, name=None):
    if _id:
        content = _helpers.base_get(
            "experiments/{0}/fcsfiles/{1}".format(experiment_id, _id)
        )
        content = FcsFile(properties=content)
    else:
        content = _helpers.load_fcsfile_by_name(experiment_id, name)
    return content


def validate_response(res):
    try:
        keys = [
            "experimentId",
            "name",
            "type",
            "gid",
            "xChannel",
            "yChannel",
            "tailoredPerFile",
            "fcsFileId",
            "parentPopulationId",
            "model",
        ]
        assert all([key in res.keys() for key in keys])
    except:
        raise RuntimeError("Invalid request: {}".format(res))
