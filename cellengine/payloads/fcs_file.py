import attr
import pandas
import fcsparser
from typing import List, Dict

from cellengine.utils.helpers import GetSet


@attr.s(repr=False, slots=True)
class _FcsFile(object):
    """A class representing a CellEngine FCS file."""

    def __repr__(self):
        return "FcsFile(_id='{}', name='{}')".format(self._id, self.name)

    _properties = attr.ib(default={}, repr=False)

    _events = attr.ib(default=None)

    name = GetSet("filename")

    _id = GetSet("_id", read_only=True)

    experiment_id = GetSet("experimentId", read_only=True)

    panel_name = GetSet("panelName")

    event_count = GetSet("eventCount", read_only=True)

    has_file_internal_comp = GetSet("hasFileInternalComp", read_only=True)

    header = GetSet("header", read_only=True)

    is_control = GetSet("isControl")

    size = GetSet("size")

    sample_name = GetSet("sampleName", read_only=True)

    spill_string = GetSet("spillString", read_only=True)

    md5 = GetSet("md5")

    crc32c = GetSet("crc32c", read_only=True)

    filename = GetSet("filename")

    # TODO: make this a Munch class
    panel = GetSet("panel")

    compensation = GetSet("compensation")

    @property
    def annotations(self):
        """Return file annotations.
        New annotations may be added with file.annotations.append or
        redefined by setting file.annotations to a dict with a 'name'
        and 'value' key (i.e. {'name': 'plate row', 'value': 'A'}) or
        a list of such dicts.
        """
        return self._properties["annotations"]

    @annotations.setter
    def annotations(self, val):
        if type(val) is not dict or "name" and "value" not in val:
            raise TypeError('Input must be a dict with a "name" and a "value" item.')
        else:
            get_input = input("This will overwrite current annotations. Confirm y/n: ")
            if "y" in get_input.lower():
                self._properties["annotations"] = val

    @property
    def events(self):
        pass

    #     """A DataFrame containing this file's data. This is fetched
    #     from the server on-demand the first time that this property is accessed.
    #     """
    #     if self._events is None:
    #         fresp = base_get(
    #             "/experiments/{0}/fcs_files/{1}.fcs".format(self.experiment_id, self._id)
    #         )
    #         parser = fcsparser.api.FCSParser.from_data(fresp.content)
    #         self._events = pandas.DataFrame(parser.data, columns=parser.channel_names_n)
    #     return self._events

    @property
    def channels(self) -> List:
        """Return all channels in the file"""
        return [f["channel"] for f in self.panel]

    @events.setter
    def events(self, val):
        self.__dict__["_events"] = val