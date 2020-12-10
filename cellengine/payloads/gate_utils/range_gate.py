import numpy

from cellengine.utils.generate_id import generate_id
from cellengine.payloads.gate_utils import format_common_gate


def format_range_gate(
    experiment_id,
    x_channel,
    name,
    x1,
    x2,
    y=0.5,
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
    """Formats a range gate for posting to the CE API.

    Args:
        experiment_id: The ID of the experiment to which to add the gate.
            Use when calling this as a static method; not needed when calling
            from an Experiment object
        x_channel: The name of the x channel to which the gate applies.
        name: The name of the gate
        x1: The first x coordinate (after the channel's scale has been applied).
        x2: The second x coordinate (after the channel's scale has been applied).
        y: Position of the horizontal line between the vertical lines
        label: Position of the label. Defaults to the midpoint of the gate.
        gid: Group ID of the gate, used for tailoring. If this is not
            specified, then a new Group ID will be created. To create a
            tailored gate, the gid of the global tailored gate must be specified.
        locked: Prevents modification of the gate via the web interface.
        parent_population_id: ID of the parent population. Use ``None`` for
            the "ungated" population. If specified, do not specify
            ``parent_population``.
        parent_population: Name of the parent population. An attempt will
            be made to find the population by name.  If zero or more than
            one population exists with the name, an error will be thrown.
            If specified, do not specify ``parent_population_id``.
        tailored_per_file: Whether or not this gate is tailored per FCS file.
        fcs_file_id: ID of FCS file, if tailored per file. Use ``None`` for
            the global gate in a tailored gate group. If specified, do not
            specify ``fcs_file``.
        fcs_file: Name of FCS file, if tailored per file. An attempt will be made
            to find the file by name. If zero or more than one file exists with
            the name, an error will be thrown. Looking up files by name is
            slower than using the ID, as this requires additional requests
            to the server. If specified, do not specify ``fcs_file_id``.
        create_population: Automatically create corresponding population.

    Returns:
        A RangeGate object.

    Example:
        experiment.create_range_gate(x_channel="FSC-A", name="my gate",
        x1=12.502, x2=95.102)
        cellengine.Gate.create_range_gate(experiment_id,
        x_channel="FSC-A", name="my gate",
        12.502, 95.102)
    """
    if label == []:
        label = [numpy.mean([x1, x2]), y]
    if gid is None:
        gid = generate_id()

    model = {"locked": locked, "label": label, "range": {"x1": x1, "x2": x2, "y": y}}

    body = {
        "experimentId": experiment_id,
        "name": name,
        "type": "RangeGate",
        "gid": gid,
        "xChannel": x_channel,
        "parentPopulationId": parent_population_id,
        "model": model,
    }

    return format_common_gate(
        experiment_id,
        body=body,
        tailored_per_file=tailored_per_file,
        fcs_file_id=fcs_file_id,
        fcs_file=fcs_file,
        create_population=create_population,
    )
