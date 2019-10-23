from custom_inherit import doc_inherit
from .. import _helpers
from .gate_util import common_gate_create, gate_style


@doc_inherit(common_gate_create, style=gate_style)
def create_split_gate(experiment_id, x_channel, name,
                      x, y, labels=[], gid=None, gids=None, locked=False,
                      parent_population_id=None, parent_population=None,
                      tailored_per_file=False, fcs_file_id=None,
                      fcs_file=None, create_population=True):
    """
    Creates a split gate. Split gates have two sectors (right and left),
    each with a unique gid and name.

    Args:
        x: The x coordinate of the center point (after the channel's scale has
            been applied).  y: The y coordinate of the dashed line extending from
            the center point (after the channel's scale has been applied).
        labels: Positions of the quadrant labels. A list of two length-2 lists in
            the order: L, R. These are set automatically to the top corners.
        gids: Group IDs of each sector, assigned to model.gids.

    Returns:
        A SplitGate object.

    Example:
        cellengine.Gate.create_split_gate(experiment_id, x_channel="FSC-A",
        name="my gate", x=144000, y=100000)
        experiment.create_split_gate(x_channel="FSC-A", name="my gate", x=144000,
            y=100000)
        """
    # set labels based on axis scale
    r = _helpers.base_get(f'experiments/{experiment_id}/scalesets')[0]
    scale_min = min(x['scale']['minimum'] for x in r['scales'])
    scale_max = max(x['scale']['minimum'] for x in r['scales'])

    if labels == []:
        labels = [[scale_min + 0.1 * scale_max, 0.916],
                  [scale_max - 0.1 * scale_max, 0.916]]
    elif len(labels) == 2 and len(labels[0]) == 2 and len(labels[1]) == 2:
        pass
    else:
        raise ValueError('Labels must be a list of two length-2 lists.')

    if gid is None:
        gid = _helpers.generate_id()
        if gids is None:
            gids = [_helpers.generate_id(), _helpers.generate_id()]

    names = [name + ' (L)', name + ' (R)']

    model = {
        'locked': locked,
        'labels': labels,
        'gids': gids,
        'split': {'x': x, 'y': y}
    }

    body = {
        'experimentId': experiment_id,
        'names': names,
        'type': 'SplitGate',
        'gid': gid,
        'xChannel': x_channel,
        'parentPopulationId': parent_population_id,
        'model': model
    }

    return common_gate_create(experiment_id, body=body,
                              tailored_per_file=tailored_per_file,
                              fcs_file_id=fcs_file_id,
                              fcs_file=fcs_file, create_population=create_population)
