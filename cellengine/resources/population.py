from __future__ import annotations
import cellengine as ce
from cellengine.payloads.population import _Population


class Population(_Population):
    @classmethod
    def get(cls, experiment_id: str, _id: str = None, name: str = None) -> Population:
        kwargs = {"name": name} if name else {"_id": _id}
        return ce.APIClient().get_population(experiment_id, **kwargs)

    @classmethod
    def create(cls, experiment_id: str, population: dict) -> Population:
        return ce.APIClient().post_population(experiment_id, population)

    def update(self):
        """Save changes to this Population to CellEngine."""
        res = ce.APIClient().update_entity(
            self.experiment_id, self._id, "populations", self._properties
        )
        self._properties.update(res)

    def delete(self):
        ce.APIClient().delete_entity(self.experiment_id, "populations", self._id)
