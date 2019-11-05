cellengine = __import__(__name__.split(".")[0])
import attr
from .client import session
from . import _helpers


@attr.s(repr=False)
class Population(object):
    """
    A class representing a CellEngine population.

    Attributes
        _properties (:obj:`dict`): Population properties; reqired.
    """

    def __repr__(self):
        return "Population(_id='{0}', name='{1}')".format(self._id, self.name)

    _properties = attr.ib()

    _id = _helpers.GetSet("_id", read_only=True)

    name = _helpers.GetSet("name")

    experiment_id = _helpers.GetSet("experimentId", read_only=True)

    gates = _helpers.GetSet("gates")

    terminal_gate_gid = _helpers.GetSet("terminalGateId")

    parent_id = _helpers.GetSet("parentId")

    unique_name = _helpers.GetSet("uniqueName", read_only=True)

    def update(self):
        """Save any changed data to CellEngine."""
        return _helpers.base_update(
            "experiments/{0}/populations/{1}".format(self.experiment_id, self._id),
            body=self._properties,
            classname=Population,
        )

    # delete
    def delete(self):
        return _helpers.base_delete(
            "experiments/{0}/populations/{1}".format(self.experiment_id, self._id)
        )

    def create_child_rectangle_gate(
        self,
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
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_rectangle_gate(
            self.experiment_id,
            x_channel,
            y_channel,
            name,
            x1,
            x2,
            y1,
            y2,
            label=label,
            gid=gid,
            locked=locked,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
            create_population=True,
            parent_population_id=self._id,
        )

    def create_child_ellipse_gate(
        self,
        x_channel,
        y_channel,
        name,
        x,
        y,
        angle,
        major,
        minor,
        label=[],
        gid=None,
        locked=False,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_ellipse_gate(
            self.experiment_id,
            x_channel,
            y_channel,
            name,
            x,
            y,
            angle,
            major,
            minor,
            label=label,
            gid=gid,
            locked=locked,
            parent_population_id=self._id,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
        )

    def create_child_polygon_gate(
        self,
        x_channel,
        y_channel,
        name,
        x_vertices,
        y_vertices,
        label=[],
        gid=None,
        locked=False,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_polygon_gate(
            self.experiment_id,
            x_channel,
            y_channel,
            name,
            x_vertices,
            y_vertices,
            label=label,
            gid=gid,
            locked=locked,
            parent_population_id=self._id,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
        )

    def create_child_range_gate(
        self,
        x_channel,
        name,
        x1,
        x2,
        label=[],
        gid=None,
        locked=False,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_range_gate(
            self.experiment_id,
            x_channel,
            name,
            x1,
            x2,
            label=label,
            gid=gid,
            locked=locked,
            parent_population_id=self._id,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
        )

    def create_child_quadrant_gate(
        self,
        x_channel,
        y_channel,
        name,
        x,
        y,
        labels=[],
        gid=None,
        gids=None,
        locked=False,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_quadrant_gate(
            self.experiment_id,
            x_channel,
            y_channel,
            name,
            x,
            y,
            labels=labels,
            gid=gid,
            gids=gids,
            locked=locked,
            parent_population_id=self._id,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
        )

    def create_child_split_gate(
        self,
        x_channel,
        name,
        x,
        y,
        labels=[],
        gid=None,
        gids=None,
        locked=False,
        tailored_per_file=False,
        fcs_file_id=None,
        fcs_file=None,
    ):

        return cellengine.Gate.create_split_gate(
            self.experiment_id,
            x_channel,
            name,
            x,
            y,
            labels=labels,
            gid=gid,
            gids=gids,
            locked=locked,
            parent_population_id=self._id,
            tailored_per_file=tailored_per_file,
            fcs_file_id=fcs_file_id,
            fcs_file=fcs_file,
        )
