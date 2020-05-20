import json
import pytest
import responses
from cellengine.utils.generate_id import generate_id
from cellengine.resources.fcsfile import FcsFile


EXP_ID = "5d38a6f79fae87499999a74b"
FCSFILE_ID = "5d64abe2ca9df61349ed8e7c"


@responses.activate
def test_should_get_fcs_file(ENDPOINT_BASE, client, fcsfiles):
    file_id = fcsfiles[0]["_id"]
    responses.add(
        responses.GET,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles/{file_id}",
        json=fcsfiles[0],
    )
    file = FcsFile.get(EXP_ID, file_id)
    assert type(file) is FcsFile


@responses.activate
def test_should_upload_fcsfile(ENDPOINT_BASE, client, fcsfiles):
    """Test upload of a new fcsfile.
    This test must be run from the project root directory"""
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles",
        json=fcsfiles[0],
    )
    file = FcsFile.upload(EXP_ID, "tests/data/text.txt")


@responses.activate
def test_should_create_fcsfile(ENDPOINT_BASE, client, fcsfiles):
    """Test upload of a new fcsfile.
    This test must be run from the project root directory"""
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles",
        json=fcsfiles[1],
    )
    file = FcsFile.create(EXP_ID, [fcsfiles[0]["_id"]], "new file")
    assert json.loads(responses.calls[0].request.body) == {
        "fcsFiles": ["5d64abe2ca9df61349ed8e79"],
        "filename": "new file",
    }


params = [
    (FCSFILE_ID, [FCSFILE_ID]),
    ([FCSFILE_ID], [FCSFILE_ID]),
    (
        ["fcsfile_id_1", "fcsfile_id_2", "fcsfile_id_3"],
        ["fcsfile_id_1", "fcsfile_id_2", "fcsfile_id_3"],
    ),
    ({EXP_ID: FCSFILE_ID}, [{EXP_ID: FCSFILE_ID}]),
    ([{EXP_ID: FCSFILE_ID}], [{EXP_ID: FCSFILE_ID}]),
]


@pytest.mark.parametrize("fcsfile_args,expected_response", params)
@responses.activate
def test_should_create_fcsfile_and_correctly_parse_fcsfile_args(
    ENDPOINT_BASE, client, fcsfiles, fcsfile_args, expected_response
):
    """Test upload of a new fcsfile.
    This test must be run from the project root directory"""
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles",
        json=fcsfiles[1],
    )
    file = FcsFile.create(EXP_ID, fcsfile_args, "new file")
    assert json.loads(responses.calls[0].request.body) == {
        "fcsFiles": expected_response,
        "filename": "new file",
    }


@responses.activate
def test_should_create_fcsfile_and_correctly_parse_body_args(
    ENDPOINT_BASE, client, fcsfiles
):
    """Test upload of a new fcsfile.
    This test must be run from the project root directory"""
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles",
        json=fcsfiles[1],
    )
    file = FcsFile.create(
        EXP_ID,
        FCSFILE_ID,
        "new name",
        add_file_number=True,
        add_event_number=True,
        pre_subsample_n=1,
        pre_subsample_p=1,
    )
    assert json.loads(responses.calls[0].request.body) == {
        "fcsFiles": [FCSFILE_ID],
        "filename": "new name",
        "addFileNumber": True,
        "addEventNumber": True,
        "preSubsampleN": 1,
        "preSubsampleP": 1
        # leave out "seed" to test param not specified
    }


@responses.activate
def test_should_delete_fcsfile(ENDPOINT_BASE, client, fcsfiles):
    fcsfile = FcsFile(fcsfiles[0])
    responses.add(
        responses.DELETE,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles/{fcsfile._id}",
    )
    deleted = fcsfile.delete()
    assert deleted is None


@responses.activate
def test_fcs_file_and_fcs_file_id_defined(
    ENDPOINT_BASE, experiment, experiments, gates
):
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=gates[0],
    )
    with pytest.raises(
        ValueError, match="Please specify only 'fcs_file' or 'fcs_file_id'."
    ):
        experiment.create_rectangle_gate(
            "FSC-A",
            "FSC-W",
            "fcs_rect_gate",
            x1=1,
            x2=2,
            y1=3,
            y2=4,
            fcs_file="Specimen_001_A1_A01.fcs",
            fcs_file_id="5d38a7159fae87499999a74e",
            tailored_per_file=True,
        )


@responses.activate
def test_tailored_per_file_true(ENDPOINT_BASE, experiment, rectangle_gate):
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=rectangle_gate,
    )
    new_gate = experiment.create_rectangle_gate(
        "FSC-A",
        "FSC-W",
        "fcs_rect_gate",
        x1=1,
        x2=2,
        y1=3,
        y2=4,
        tailored_per_file=True,
    )
    assert json.loads(responses.calls[0].request.body)["tailoredPerFile"] is True


@responses.activate
def test_fcs_file_id_is_None_and_fcs_file_is_None(
    ENDPOINT_BASE, experiment, rectangle_gate
):
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=rectangle_gate,
    )
    res = experiment.create_rectangle_gate(
        "FSC-A", "FSC-W", "fcs_rect_gate", x1=1, x2=2, y1=3, y2=4
    )
    assert json.loads(responses.calls[0].request.body)["fcsFileId"] is None


@responses.activate
def test_create_global_tailored_gate(ENDPOINT_BASE, experiment, rectangle_gate):
    global_gid = generate_id()
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=rectangle_gate,
    )
    res = experiment.create_rectangle_gate(
        x_channel="FSC-A",
        y_channel="FSC-W",
        name="fcs_rect_gate",
        x1=1,
        x2=2,
        y1=3,
        y2=4,
        tailored_per_file=True,
        gid=global_gid,
    )
    assert json.loads(responses.calls[0].request.body)["tailoredPerFile"] is True
    assert json.loads(responses.calls[0].request.body)["gid"] == global_gid


@responses.activate
def test_specify_fcs_file_id(ENDPOINT_BASE, experiment, rectangle_gate):
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=rectangle_gate,
    )
    res = experiment.create_rectangle_gate(
        x_channel="FSC-A",
        y_channel="FSC-W",
        name="fcs_rect_gate",
        x1=1,
        x2=2,
        y1=3,
        y2=4,
        fcs_file_id="5d38a7159fae87499999a751",
        tailored_per_file=True,
    )
    assert (
        json.loads(responses.calls[0].request.body)["fcsFileId"]
        == "5d38a7159fae87499999a751"
    )


@responses.activate
def test_fcs_file_called_by_name(ENDPOINT_BASE, experiment, fcsfiles, rectangle_gate):
    responses.add(
        responses.GET,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles",
        json=[fcsfiles[3]],
    )
    responses.add(
        responses.GET,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/fcsfiles/5d64abe2ca9df61349ed8e7c",
        json=fcsfiles[3],
    )
    responses.add(
        responses.POST,
        ENDPOINT_BASE + f"/experiments/{EXP_ID}/gates",
        status=201,
        json=rectangle_gate,
    )
    res = experiment.create_rectangle_gate(
        "FSC-A",
        "FSC-W",
        "fcs_rect_gate",
        x1=1,
        x2=2,
        y1=3,
        y2=4,
        fcs_file="Specimen_001_A1_A01.fcs",
        tailored_per_file=True,
    )
    assert json.loads(responses.calls[2].request.body)["tailoredPerFile"] is True
    assert (
        json.loads(responses.calls[2].request.body)["fcsFileId"]
        == "5d64abe2ca9df61349ed8e7c"
    )
