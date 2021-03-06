from __future__ import annotations
import os
import json
import pandas
from getpass import getpass
from typing import Dict, List, Union, Optional
from functools import lru_cache
from requests_toolbelt.multipart.encoder import MultipartEncoder

from cellengine.utils.api_client.BaseAPIClient import BaseAPIClient
from cellengine.utils.api_client.APIError import APIError
from cellengine.utils.singleton import Singleton
from ...resources.attachment import Attachment
from ...resources.compensation import Compensation
from ...resources.experiment import Experiment
from ...resources.fcs_file import FcsFile
from ...resources.gate import Gate
from ...resources.plot import Plot
from ...resources.population import Population
from ...resources.scaleset import ScaleSet


class APIClient(BaseAPIClient, metaclass=Singleton):
    _API_NAME = "CellEngine Python Toolkit"

    def __init__(self, username=None, password=None, token=None):
        super(APIClient, self).__init__()
        self.base_url = os.environ.get(
            "CELLENGINE_BASE_URL", "https://cellengine.com/api/v1"
        )
        self.username = username
        self.password = password or os.environ.get("CELLENGINE_PASSWORD")
        self.token = token or os.environ.get("CELLENGINE_AUTH_TOKEN")
        self.user_id = None
        self.flags = None
        self.authenticated = self._authenticate(
            self.username, self.password, self.token
        )

        self.cache_info = self._get_id_by_name.cache_info
        self.cache_clear = self._get_id_by_name.cache_clear

    def __repr__(self):
        if self.username:
            return f"Client(user={self.username})"
        else:
            return "Client(TOKEN)"

    def _authenticate(self, username, password, token):
        """Authenticate with the CellEngine API.

        There are two ways of authenticating:
            1. Username and password. Use this to authenticate a user.
            2. API token. Use this to authenticate an application that is
                not associated with a user, such as a LIMS integration.

        Args:
            username: Login credential set during CellEngine registration
            password: Password for login
            token: Authentication token; may be passed instead of username and password
        """
        if username:
            self.username = username
            self.password = password or getpass()

            res = self._post(
                f"{self.base_url}/signin",
                {"username": self.username, "password": self.password},
            )

            self.token = res["token"]
            os.environ["CELLENGINE_AUTH_TOKEN"] = self.token
            self.user_id = res["userId"]
            self.flags = res["flags"]

        elif token:
            self.requests_session.cookies.update({"token": "{0}".format(token)})

        else:
            raise APIError("Authentication failed: Username or token must be provided.")
        return True

    @lru_cache(maxsize=None)
    def _get_id_by_name(self, name, resource_type, experiment_id):
        if resource_type != "experiments":
            path = f"experiments/{experiment_id}/{resource_type}"
        else:
            path = "experiments"
        if (resource_type == "fcsfiles") or (resource_type == "attachments"):
            query = "filename"
        else:
            query = "name"
        res = self._lookup_by_name(path, query, name)
        try:
            return self._handle_response(res)["_id"]
        except RuntimeError as e:
            raise RuntimeError(str(e).format(name))

    def _lookup_by_name(self, path, query, name):
        params = f'query=eq({query},"{name}")&limit=2'
        return self._get(f"{self.base_url}/{path}", params=params)

    def _handle_response(self, response):
        if type(response) is list:
            self._handle_list(response)
        else:
            response = [response]
        return response[0]

    def _handle_list(self, response: List) -> RuntimeError:
        if len(response) == 0:
            raise RuntimeError("Resource with the name '{}' does not exist.")
        elif len(response) > 1:
            raise RuntimeError("More than one resource with the name '{}' exists.")

    def update_entity(self, experiment_id, _id, entity_type, body) -> dict:
        return self._patch(
            f"{self.base_url}/experiments/{experiment_id}/{entity_type}/{_id}",
            json=body,
        )

    def delete_entity(self, experiment_id, entity_type, _id):
        url = f"{self.base_url}/experiments/{experiment_id}/{entity_type}/{_id}"
        self._delete(url)

    def get_attachments(self, experiment_id) -> List[Attachment]:
        attachments = self._get(
            f"{self.base_url}/experiments/{experiment_id}/attachments"
        )
        return [Attachment(attachment) for attachment in attachments]

    def download_attachment(self, experiment_id, _id=None, name=None) -> Attachment:
        """Download an attachment"""
        _id = _id or self._get_id_by_name(name, "attachments", experiment_id)
        attachment = self._get(
            f"{self.base_url}/experiments/{experiment_id}/attachments/{_id}", raw=True,
        )
        return attachment

    def get_attachment(self, experiment_id, _id=None, name=None) -> Attachment:
        attachments = self.get_attachments(experiment_id)
        try:
            return [a for a in attachments if (a.filename == name) or (a._id == _id)][0]
        except IndexError:
            raise APIError("No experiment with that name or _id found.")

    def post_attachment(
        self, experiment_id, filepath: str, filename: str = None
    ) -> Attachment:
        """Upload an attachment

        Args:
            filepath (str): Local path to file to upload.
            filename (str, optional): Optionally, specify a new name for the file.

        Returns:
            The newly-uploaded Attachment
        """
        url = f"{self.base_url}/experiments/{experiment_id}/attachments"
        file, headers = self._read_multipart_file(url, filepath, filename)
        return Attachment(self._post(url, data=file, headers=headers))

    def get_compensations(self, experiment_id, as_dict=False) -> List[Compensation]:
        compensations = self._get(
            f"{self.base_url}/experiments/{experiment_id}/compensations"
        )
        if as_dict:
            return compensations
        return [Compensation(comp) for comp in compensations]

    def get_compensation(
        self, experiment_id, _id=None, name=None, as_dict=False
    ) -> Compensation:
        _id = _id or self._get_id_by_name(name, "compensations", experiment_id)
        comp = self._get(
            f"{self.base_url}/experiments/{experiment_id}/compensations/{_id}"
        )
        if as_dict:
            return comp
        return Compensation(comp)

    def post_compensation(self, experiment_id, compensation=None) -> Compensation:
        res = self._post(
            f"{self.base_url}/experiments/{experiment_id}/compensations",
            json=compensation,
        )
        return Compensation(res)

    def get_experiments(self, as_dict=False) -> List[Experiment]:
        experiments = self._get(f"{self.base_url}/experiments")
        if as_dict:
            return experiments
        return [Experiment(experiment) for experiment in experiments]

    def get_experiment(self, _id=None, name=None, as_dict=False) -> Experiment:
        _id = _id or self._get_id_by_name(name, "experiments", _id)
        experiment = self._get(f"{self.base_url}/experiments/{_id}")
        if as_dict:
            return experiment
        return Experiment(experiment)

    def post_experiment(self, experiment: dict, as_dict=False) -> Experiment:
        """Create a new experiment on CellEngine."""
        experiment = self._post(f"{self.base_url}/experiments", json=experiment)
        if as_dict:
            return experiment
        return Experiment(experiment)

    def clone_experiment(self, _id, name=None, as_dict=False) -> Experiment:
        experiment = self._post(
            f"{self.base_url}/experiments/{_id}/clone", json={"name": name}
        )
        if as_dict:
            return experiment
        return Experiment(experiment)

    def update_experiment(self, _id, body) -> Dict:
        return self._patch(f"{self.base_url}/experiments/{_id}", json=body)

    def delete_experiment(self, _id):
        """Hard-delete an experiment.

        Warning: This action is irreversible!
        """
        self._delete(f"{self.base_url}/experiments/{_id}")

    def get_fcs_files(self, experiment_id, as_dict=False) -> List[FcsFile]:
        fcs_files = self._get(f"{self.base_url}/experiments/{experiment_id}/fcsfiles")
        if as_dict:
            return fcs_files
        return [FcsFile(fcs_file) for fcs_file in fcs_files]

    def get_fcs_file(
        self, experiment_id, _id=None, name=None, as_dict=False
    ) -> FcsFile:
        _id = _id or self._get_id_by_name(name, "fcsfiles", experiment_id)
        fcs_file = self._get(
            f"{self.base_url}/experiments/{experiment_id}/fcsfiles/{_id}"
        )
        if as_dict:
            return fcs_file
        return FcsFile(fcs_file)

    def upload_fcs_file(
        self, experiment_id, filepath: str, filename: str = None
    ) -> FcsFile:
        """Upload an FCS file to CellEngine

        Args:
            filepath (str): Local path to FCS file.
            filename (str, optional): Optionally, specify a new name for the file.

        Returns:
            The newly-uploaded FcsFile
        """
        url = f"{self.base_url}/experiments/{experiment_id}/fcsfiles"
        file, headers = self._read_multipart_file(url, filepath, filename)
        return FcsFile(self._post(url, data=file, headers=headers))

    def _read_multipart_file(self, url, filepath: str, filename: str = None):
        """Posts a MultipartEncoder of the file and its content-type"""
        filename = filename or os.path.basename(filepath)
        mpe = MultipartEncoder(
            fields={
                "data": (filename, open(filepath, "rb"), "application/octet-stream")
            }
        )
        return mpe, {"Content-Type": mpe.content_type}

    def create_fcs_file(self, experiment_id, body):
        """Creates an FCS file by copying, concatenating and/or
        subsampling existing file(s) from this or other experiments. Can be
        used to import files from other experiments.
        """
        url = f"{self.base_url}/experiments/{experiment_id}/fcsfiles"
        return FcsFile(self._post(url, json=body))

    def download_fcs_file(self, experiment_id: str, fcs_file_id: str, **kwargs):
        """Download events for a specific FcsFile

        Parameters:
            experiment_id (str): ID of the experiment
            fcs_file_id (str): ID of the FcsFile
            kwargs:
                - compensatedQ (bool): If true, applies the compensation
                  specified in compensationId to the exported events. For
                  TSV format, the numerical values will be the compensated
                  values.  For FCS format, the numerical values will be
                  unchanged, but the file header will contain the
                  compensation as the spill string (file-internal
                  compensation).
                - compensationId (str, optional): Required if populationId is
                    specified. Compensation to use for gating.
                - headers (bool): For TSV format only. If true, a header row
                  containing the channel names will be included.
                - original (bool): If true, the returned file will be
                    byte-for-byte identical to the originally uploaded
                    file. If false or unspecified (and compensatedQ is
                    false, populationId is unspecified and all subsampling
                    parameters are unspecified), the returned file will
                    contain essentially the same data as the originally
                    uploaded file, but may not be byte-for-byte identical.
                    For example, the byte ordering of the DATA segment will
                    always be little-endian and any extraneous information
                    appended to the end of the original file will be
                    stripped. This parameter takes precedence over
                    compensatedQ, populationId and the subsampling
                    parameters.
                - populationId (str): If provided, only events from this
                    population will be included in the output file.
                - postSubsampleN (int): Randomly subsample the file to
                    contain this many events after gating.
                - postSubsampleP (float): Randomly subsample the file to
                    contain this percent of events (0 to 1) after gating.
                - preSubsampleN (int): Randomly subsample the file to contain
                    this many events before gating.
                - preSubsampleP (float): Randomly subsample the file to
                    contain this percent of events (0 to 1) before gating.
                - seed: (int): Seed for random number generator used for
                    subsampling. Use for deterministic (reproducible)
                    subsampling.  If omitted, a pseudo-random value is
                    used.
                - addEventNumber (bool): Add an event number column to the
                    exported file. When a populationId is specified
                    (when gating), this number corresponds to the index of
                    the event in the original file.
        """
        params = {}
        if kwargs:
            params = dict(kwargs)

        return self._get(
            f"{self.base_url}/experiments/{experiment_id}/fcsfiles/{fcs_file_id}.fcs",
            params=params,
            raw=True,
        )

    def get_gates(self, experiment_id, as_dict=False) -> List[Gate]:
        gates = self._get(f"{self.base_url}/experiments/{experiment_id}/gates")
        if as_dict:
            return gates
        return [Gate.factory(gate) for gate in gates]

    def get_gate(self, experiment_id: str, _id, as_dict=False) -> Gate:
        """Gates cannot be retrieved by name."""
        gate = self._get(f"{self.base_url}/experiments/{experiment_id}/gates/{_id}")
        if as_dict:
            return gate
        return Gate.factory(gate)

    def delete_gate(
        self, experiment_id: str, _id: str = None, gid: str = None, exclude: str = None
    ) -> None:
        """Deletes a gate or a tailored gate family.

        Specify the top-level gid when working with compound gates (specifying
        the gid of a sector (i.e. one listed in ``model.gids``) will result in no
        gates being deleted). If ``_id`` is specified, only that gate will be
        deleted, regardless of the other parameters specified. May be called as
        a static method from cellengine.Gate or from an Experiment instance.

        Args:
            experiment_id: ID of experiment.
            _id: ID of the gate to delete.
            gid: ID of gate family to delte.
            exclude: Gate ID to exclude from deletion.

        Example:
            ```python
            cellengine.Gate.delete_gate(experiment_id, gid = [gate family ID])
            # or
            experiment.delete_gate(_id = [gate ID])
            ```

        Returns:
            None
        """
        if _id:
            url = f"{self.base_url}/experiments/{experiment_id}/gates/{_id}"
        elif gid:
            url = f"{self.base_url}/experiments/{experiment_id}/gates?gid={gid}"
            if exclude:
                url = "{0}%exclude={1}".format(url, exclude)
        else:
            raise ValueError("Either _id or gid must be specified.")
        self._delete(url)

    def post_gate(
        self, experiment_id, gate: Dict, create_population=True, as_dict=False
    ) -> Gate:
        res = self._post(
            f"{self.base_url}/experiments/{experiment_id}/gates",
            json=gate,
            params={"createPopulation": create_population},
        )
        if as_dict:
            return res
        if type(res) is list:
            return [Gate.factory(r) for r in res]
        return Gate.factory(res)

    def update_gate_family(self, experiment_id, gid, body: dict = None) -> dict:
        return self._patch(
            f"{self.base_url}/experiments/{experiment_id}/gates?gid={gid}", json=body,
        )

    def tailor_to(self, experiment_id, gate_id, fcs_file_id):
        """Tailor a gate to a file."""
        gate = self.get_gate(experiment_id, gate_id)
        gate._properties["tailoredPerFile"] = True
        gate._properties["fcsFileId"] = fcs_file_id
        return self.update_entity(experiment_id, gate_id, "gates", gate._properties)

    def get_plot(
        self,
        experiment_id,
        fcs_file_id,
        x_channel: str,
        y_channel: str,
        plot_type: str,
        population_id: str = None,
        properties: Dict = None,
        raw=False,
    ) -> Plot:

        req_params = {
            "fcsFileId": fcs_file_id,
            "xChannel": x_channel,
            "yChannel": y_channel,
            "plotType": plot_type,
            "populationId": population_id,
        }

        if properties:
            req_params.update(properties)

        data = self._get(
            f"{self.base_url}/experiments/{experiment_id}/plot",
            params=req_params,
            raw=True,
        )
        if raw:
            return data
        return Plot(
            experiment_id,
            fcs_file_id,
            x_channel,
            y_channel,
            plot_type,
            population_id,
            data,
        )

    def get_populations(self, experiment_id, as_dict=False) -> List[Population]:
        populations = self._get(
            f"{self.base_url}/experiments/{experiment_id}/populations"
        )
        if as_dict:
            return populations
        return [Population(pop) for pop in populations]

    def get_population(
        self, experiment_id, _id=None, name=None, as_dict=False
    ) -> Population:
        _id = _id or self._get_id_by_name(name, "populations", experiment_id)
        population = self._get(
            f"{self.base_url}/experiments/{experiment_id}/populations/{_id}"
        )
        if as_dict:
            return population
        return Population(population)

    def post_population(self, experiment_id, population: Dict) -> Gate:
        res = self._post(
            f"{self.base_url}/experiments/{experiment_id}/populations", json=population,
        )
        return Population(res)

    def get_scaleset(self, experiment_id, as_dict=False) -> ScaleSet:
        """Get a scaleset for an experiment."""
        scaleset = self._get(f"{self.base_url}/experiments/{experiment_id}/scalesets")[
            0
        ]
        if as_dict:
            return scaleset
        return ScaleSet(scaleset)

    def post_statistics(self, experiment_id, req_params, raw=True):
        return self._post(
            f"{self.base_url}/experiments/{experiment_id}/bulkstatistics",
            json=req_params,
            raw=raw,
        )

    def get_statistics(
        self,
        experiment_id: str,
        statistics: Union[str, List[str]],
        channels: List[str],
        q: float = None,
        annotations: Optional[bool] = False,
        compensation_id: Optional[str] = None,
        fcs_file_ids: Optional[List[str]] = None,
        format: Optional[str] = "json",
        layout: Optional[str] = None,
        percent_of: Optional[Union[str, List[str]]] = "PARENT",
        population_ids: Optional[List[str]] = None,
    ):
        def determine_format(f):
            if f == "pandas":
                return "json"
            else:
                return f

        if "quantile" == statistics:
            try:
                assert q
            except AssertionError:
                raise ValueError(
                    "'q' is a required parameter for 'quantile' statistics."
                )

        params = {
            "statistics": statistics,
            "q": q,
            "channels": channels,
            "annotations": annotations,
            "compensationId": compensation_id,
            "fcsFileIds": fcs_file_ids,
            "format": determine_format(format),
            "layout": layout,
            "percentOf": percent_of,
            "populationIds": population_ids,
        }
        req_params = {key: val for key, val in params.items() if val is not None}

        raw_stats = self.post_statistics(experiment_id, req_params)

        format = format.lower()
        if format == "json":
            return json.loads(raw_stats)
        elif "sv" in format:
            try:
                return raw_stats.decode()
            except Exception as e:
                raise ValueError("Invalid output format {}".format(format), e)
        elif format == "pandas":
            try:
                return pandas.DataFrame.from_dict(json.loads(raw_stats))
            except Exception as e:
                raise ValueError("Invalid data format {} for pandas".format(format), e)
