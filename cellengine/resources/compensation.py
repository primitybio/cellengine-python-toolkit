import attr
import pandas
import numpy
from cellengine.client import session
from cellengine.utils import helpers


@attr.s(repr=False, slots=True)
class Compensation(object):
    """A class representing a CellEngine compensation matrix. Can be applied to
    FCS files to compensate them.
    """

    def __repr__(self):
        return "Compensation(_id='{0}', name='{1}')".format(self._id, self.name)

    _properties = attr.ib(default={}, repr=False)

    _dataframe = attr.ib(default=None, repr=False)

    _id = helpers.GetSet("_id", read_only=True)

    name = helpers.GetSet("name")

    experiment_id = helpers.GetSet("experimentId")

    channels = helpers.GetSet("channels")

    @property
    def N(self):
        return len(self.channels)

    @property
    def dataframe(self):
        if getattr(self, "_dataframe") is not None:
            return self._dataframe
        else:
            self._dataframe = pandas.DataFrame(
                data=numpy.array(self._properties.get("spillMatrix")).reshape(
                    self.N, self.N
                ),
                columns=self.channels,
                index=self.channels,
            )
            return self._dataframe

    def dataframe_as_html(self):
        return self.dataframe._repr_html_()

    def apply(self, file, inplace=True):
        """
        Compensates the file's data.

        :type parser: :class:`cellengine.FcsFile`
        :param parser: The FCS file to compensate.

        :type inplace: bool
        :param inplace: Compensate the file's data in-place.

        :returns: If :attr:`inplace` is True, nothing, else a DataFrame.
        """
        data = file.events

        # spill -> comp by inverting
        inverted = numpy.linalg.inv(self.dataframe)

        # Calculate matrix product for channels matching between file and comp
        comped = data[self.channels].dot(inverted)
        comped.columns = self.channels

        data.update(comped)

        if inplace:
            file._events = data
        else:
            return data