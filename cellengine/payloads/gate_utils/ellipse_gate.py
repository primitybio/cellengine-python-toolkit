from typing import List

from cellengine.payloads.gate_utils import format_common_gate
from cellengine.utils.generate_id import generate_id


def format_ellipse_gate(
    experiment_id: str,
    x_channel: str,
    y_channel: str,
    name: str,
    x: float,
    y: float,
    angle: float,
    major: float,
    minor: float,
    label: List = [],
    gid: str = None,
    locked: bool = False,
    parent_population_id: str = None,
    parent_population: str = None,
    tailored_per_file: bool = False,
    fcs_file_id: str = None,
    fcs_file: str = None,
    create_population: bool = True,
):
    """Formats an ellipse gate for posting to the CellEngine API.

    Args:
        x_channel (str): The name of the x channel to which the gate applies.
        y_channel (str): The name of the y channel to which the gate applies.
        name (str): The name of the gate
        x (float): The x centerpoint of the gate.
        y (float): The y centerpoint of the gate.
        angle (float): The angle of the ellipse in radians.
        major (float): The major radius of the ellipse.
        minor (float): The minor radius of the ellipse.
        label (float, optional): Position of the label. Defaults to the
            midpoint of the gate.
        gid (str, optional): Group ID of the gate, used for tailoring. If this
            is not specified, then a new Group ID will be created. To create a
            tailored gate, the gid of the global tailored gate must be
            specified.
        locked (bool, optional): Prevents modification of the gate via the web
            interface.
        parent_population_id (Optional[str]): ID of the parent population. Use
            ``None`` for the "ungated" population. If specified, do not specify
            ``parent_population``.
        parent_population (str, optional): Name of the parent population. An
            attempt will be made to find the population by name.  If zero or
            more than one population exists with the name, an error will be
            thrown. If specified, do not specify ``parent_population_id``.
        tailored_per_file (bool, optional): Whether or not this gate is
            tailored per FCS file.  fcs_file_id (str, optional): ID of FCS
            file, if tailored per file. Use ``None`` for the global gate in a
            tailored gate group. If specified, do not specify ``fcs_file``.
        fcs_file (str, optional): Name of FCS file, if tailored per file. An
            attempt will be made to find the file by name. If zero or more than
            one file exists with the name, an error will be thrown. Looking up
            files by name is slower than using the ID, as this requires
            additional requests to the server. If specified, do not specify
            ``fcs_file_id``.
        create_population (optional, bool): Automatically create corresponding
            population.

    Returns:
        EllipseGate: An EllipseGate object.

    Examples:
        ```python
        cellengine.Gate.create_ellipse_gate(experiment_id, x_channel="FSC-A",
        y_channel="FSC-W", name="my gate", x=260000, y=64000, angle=0,
        major=120000, minor=70000)
        ```
    """
    if label == []:
        label = [x, y]
    if gid is None:
        gid = generate_id()

    model = {
        "locked": locked,
        "label": label,
        "ellipse": {"angle": angle, "major": major, "minor": minor, "center": [x, y]},
    }

    body = {
        "experimentId": experiment_id,
        "name": name,
        "type": "EllipseGate",
        "gid": gid,
        "xChannel": x_channel,
        "yChannel": y_channel,
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
