import attr
import importlib
from typing import Dict, List, Optional

import cellengine as ce
from cellengine.payloads.gate import _Gate
from cellengine.utils.api_client import APIClient


@attr.s(repr=False, slots=True)
class Gate(_Gate):
    def __init__(cls, *args, **kwargs):
        if cls is Gate:
            raise TypeError(
                "The Gate base class may not be directly instantiated. Use the .create() classmethod."
            )
        return object.__new__(cls, *args, **kwargs)

    _posted = attr.ib(default=False)

    @classmethod
    def get(
        cls, experiment_id: str, _id: Optional[str] = None, name: Optional[str] = None
    ):
        """Get a specific gate."""
        kwargs = {"name": name} if name else {"_id": _id}
        return ce.APIClient().get_gate(experiment_id, **kwargs)

    def delete(self):
        ce.APIClient().delete_gate(self.experiment_id, self._id)
        self._posted = False

    def update(self):
        """Save any changed data to CellEngine."""
        props = ce.APIClient().update_entity(
            self.experiment_id, self._id, "gates", body=self._properties
        )
        self._properties.update(props)

    def post(self):
        if self._posted is False:
            res = ce.APIClient().post_gate(
                self.experiment_id, self._properties, as_dict=True
            )
            self._properties.update(res)
            self._posted = True
        else:
            raise ValueError("Gate has already been posted to CellEngine.")

    @classmethod
    def build(cls, gates: Dict) -> List["_Gate"]:
        """Build a Gate object from a dict of properties.

        Args:
            experiment_id (str): The ID of the experiment to which to add the gate. Use
                when calling this as a static method; not needed when calling from an
                Experiment object.
            name (str): The name of the gate
            x_channel (str): The name of the x channel to which the gate applies.
            gid (str): Group ID of the gate, used for tailoring. If this is not
                specified, then a new Group ID will be created. If you wish you create
                a tailored gate, you must specify the gid of the global tailored gate.
            parent_population_id (str): ID of the parent population. Use ``None`` for
                the 'ungated' population. If specified, do not specify
                ``parent_population``.
            parent_population (str): Name of the parent population. An attempt will
                be made to find the population by name.  If zero or more than
                one population exists with the name, an error will be thrown.
                If specified, do not specify ``parent_population_id``.
            tailored_per_file (bool): Whether or not this gate is tailored per FCS file.
            fcs_file_id (str): ID of FCS file, if tailored per file. Use ``None`` for
                the global gate in a tailored gate group. If specified, do not
                specify ``fcs_file``.
            fcs_file (str): Name of FCS file, if tailored per file. An attempt will
                be made to find the file by name. If zero or more than one file exists
                with the name, an error will be thrown. Looking up files by name is
                slower than using the ID, as this requires additional requests
                to the server. If specified, do not specify ``fcs_file_id``.
            locked (bool): Prevents modification of the gate via the web interface.
            create_population (bool): Automatically create corresponding population.
            """
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
    def _create_multiple_gates(cls, gates: List, post_all=False):
        """Create an array of gates.
        Cellengine does not accept createPopulation when an array of gates is created
        """
        experiment_id = gates[0]["experimentId"]
        try:
            assert all([gate["experimentId"] == experiment_id for gate in gates])
        except Exception as e:
            raise ValueError("All gates must be posted to the same experiment", e)
        return [cls._create_gate(gate) for gate in gates]

    @staticmethod
    def delete_gates(
        experiment_id, _id: str = None, gid: str = None, exclude: str = None
    ):
        """Deletes a gate or a tailored gate family.

        Works for compound gates if you specify the top-level gid. Specifying
        the gid of a sector (i.e. one listed in ``model.gids``) will result in no
        gates being deleted.  If gateId is specified, only that gate will be
        deleted, regardless of the other parameters specified. May be called as
        a static method from cellengine.Gate or from an Experiment instance.

        Args:
            experimentId (str): ID of experiment.
            _id (str): ID of gate family.
            gateId (str): ID of gate.
            exclude (str): Gate ID to exclude from deletion.

        Example:
            ```python
            cellengine.Gate.delete_gate(experiment_id, gid = [gate family ID])
            # or
            experiment.delete_gate(_id = [gate ID])
            ```

        Returns:
            None

        """
        if (_id and gid) or (not _id and not gid):
            raise ValueError("Either the gid or the gateId must be specified")
        if _id:
            url = "/experiments/{0}/gates/{1}".format(experiment_id, _id)
        elif gid:
            url = "/experiments/{0}/gates?gid={1}".format(experiment_id, gid)
            if exclude:
                url = "{0}%exclude={1}".format(url, exclude)

        ce.APIClient()._delete(url)


class RectangleGate(Gate):
    pass


class PolygonGate(Gate):
    """Basic concrete class for polygon gates"""

    pass


class EllipseGate(Gate):
    """Basic concrete class for ellipse gates"""

    pass


class RangeGate(Gate):
    """Basic concrete class for range gates"""

    pass


class QuadrantGate(Gate):
    """Basic concrete class for quadrant gates"""


class SplitGate(Gate):
    """Basic concrete class for split gates"""

    pass
