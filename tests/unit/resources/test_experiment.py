import json
import pytest
import responses

from cellengine.utils import helpers
from cellengine.resources.experiment import Experiment
from cellengine.resources.population import Population
from cellengine.resources.fcsfile import FcsFile
from cellengine.resources.compensation import Compensation
from cellengine.resources.attachment import Attachment
from cellengine.resources.gate import Gate


EXP_ID = "5d38a6f79fae87499999a74b"
ATTACHMENT_ID = "5e3a5abf62c76b4f1b207b5b"
FCSFILE_ID = "5d64abe2ca9df61349ed8e7c"
COMPENSATION_ID = "5d64abe2ca9df61349ed8e95"
GATE_ID = "5d64abe2ca9df61349ed8e90"
POPULATION_ID = "5d3903529fae87499999a780"
STATISTICS_ID = "5d64abe2ca9df61349ed8e79"


@responses.activate
def test_all_experiment_properties(ENDPOINT_BASE, experiment):
    assert type(experiment._properties) is dict
    assert experiment._id == "5d38a6f79fae87499999a74b"
    assert experiment.name == "pytest_experiment"
    assert experiment.comments == [{"insert": "\xa0\xa0\xa0First 12 of 96 files\n\n"}]
    assert experiment.updated == helpers.timestamp_to_datetime(
        "2019-08-29T14:40:58.566Z"
    )
    assert experiment.deep_updated == helpers.timestamp_to_datetime(
        "2019-10-15T09:58:38.224Z"
    )
    assert experiment.deleted is None
    assert experiment.public is False
    assert experiment.uploader == {
        "_id": "5d366077a1789f7d6653075c",
        "username": "gegnew",
        "email": "g.egnew@gmail.com",
        "firstName": "Gerrit",
        "lastName": "Egnew",
        "fullName": "Gerrit Egnew",
        "id": "5d366077a1789f7d6653075c",
    }
    assert experiment.primary_researcher == {
        "_id": "5d366077a1789f7d6653075c",
        "username": "gegnew",
        "email": "g.egnew@gmail.com",
        "firstName": "Gerrit",
        "lastName": "Egnew",
        "fullName": "Gerrit Egnew",
        "id": "5d366077a1789f7d6653075c",
    }
    assert experiment.active_compensation == 0
    assert experiment.locked is False
    # assert experiment.clone_source_experiment  # does not exist for this exp
    # assert experiment.revision_source_experiment  # does not exist for this exp
    assert experiment.revisions == []
    assert experiment.per_file_compensations_enabled is False
    assert experiment.tags == []
    assert experiment.annotation_name_order == []
    assert experiment.annotation_table_sort_columns == []
    assert experiment.permissions == []
    assert experiment.created == helpers.timestamp_to_datetime(
        "2019-07-24T18:44:07.520Z"
    )


list_params = [
    ("attachments", Attachment),
    ("compensations", Compensation),
    ("fcsfiles", FcsFile),
    ("gates", Gate),
    ("populations", Population),
    # ("get_statistics", dict),
]


@responses.activate
@pytest.mark.parametrize("entity,_type", list_params)
def test_should_get_list_of_entities(
    ENDPOINT_BASE,
    experiment,
    attachments,
    compensations,
    fcsfiles,
    gates,
    populations,
    statistics,
    entity,
    _type,
):
    responses.add(
        responses.GET,
        ENDPOINT_BASE + f"/experiments/5d38a6f79fae87499999a74b/{entity}",
        json=eval(entity),
    )
    all_entities = getattr(experiment, entity)
    assert type(all_entities) is list
    if entity == "gates":
        assert all(
            [str(ent.__module__) == "cellengine.resources.gate" for ent in all_entities]
        )
    else:
        assert all([type(ent) is _type for ent in all_entities])


get_params = [
    ("attachments", ATTACHMENT_ID, Attachment),
    ("compensations", COMPENSATION_ID, Compensation),
    ("fcsfiles", FCSFILE_ID, FcsFile),
    ("gates", GATE_ID, Gate),
    ("populations", POPULATION_ID, Population),
]


@responses.activate
@pytest.mark.parametrize("entity,entity_id,_type", get_params)
def test_get_one_entity(
    ENDPOINT_BASE,
    experiment,
    attachments,
    compensations,
    fcsfiles,
    gates,
    populations,
    statistics,
    entity,
    entity_id,
    _type,
):
    responses.add(
        responses.GET,
        ENDPOINT_BASE + f"/experiments/5d38a6f79fae87499999a74b/{entity}/{entity_id}",
        json=eval(entity)[0],
    )
    func_name = "get_" + entity[:-1]
    _func = getattr(experiment, func_name)
    ent = _func(_id=entity_id)
    if entity == "gates":
        assert str(ent.__module__) == "cellengine.resources.gate"
    else:
        assert type(ent) is _type


@responses.activate
def test_get_statistics(ENDPOINT_BASE, experiment):
    """Tests getting statistics for an experiment"""
    responses.add(
        responses.POST,
        ENDPOINT_BASE + "/experiments/{}/bulkstatistics".format(experiment._id),
        json={"some": "json"},
    )
    experiment.get_statistics("mean", "FSC-A")
    assert (
        responses.calls[0].request.url
        == "https://cellengine.com/api/v1/experiments/5d38a6f79fae87499999a74b/bulkstatistics"
    )


@responses.activate
def test_should_create_experiment(ENDPOINT_BASE, experiment):
    """Tests updating experiment params"""
    response = experiment._properties.copy()
    response["name"] = "new_experiment"
    responses.add(
        responses.POST, ENDPOINT_BASE + "/experiments", json=response,
    )
    exp = Experiment.create("new_experiment")
    assert json.loads(responses.calls[0].request.body) == {
        "name": "new_experiment",
        "comments": None,
        "uploader": None,
        "primaryResearcher": None,
        "public": False,
        "tags": None,
    }


@responses.activate
def test_update_experiment(ENDPOINT_BASE, experiment):
    """Tests updating experiment params"""
    response = experiment._properties.copy()
    response.update({"name": "new name"})
    responses.add(
        responses.PATCH,
        ENDPOINT_BASE + "/experiments/5d38a6f79fae87499999a74b",
        json=response,
    )
    assert experiment.name == "pytest_experiment"
    experiment.name = "new name"
    experiment.update()
    assert experiment.name == "new name"
    assert json.loads(responses.calls[0].request.body) == experiment._properties
