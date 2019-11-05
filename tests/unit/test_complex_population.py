import os
import responses
from test_population import test_all_population_properties

base_url = os.environ.get("CELLENGINE_DEVELOPMENT", "https://cellengine.com/api/v1/")


# @responses.activate
# def test_create_complex_population(experiment, gates, populations):
#     responses.add(
#         responses.GET,
#         base_url + "experiments/5d38a6f79fae87499999a74b/gates",
#         json=gates,
#     )
#     responses.add(
#         responses.POST,
#         base_url + "experiments/5d38a6f79fae87499999a74b/populations",
#         status=201,
#         json=populations[0],
#     )
#     exp_gates = experiment.gates
#     base_gate = exp_gates[0]
#     and_gates = exp_gates[1:2]
#     not_gates = exp_gates[2:3]
#     or_gates = exp_gates[4]
#     xor_gates = exp_gates[5]
#     complex_pop = experiment.create_complex_population(
#         name="complex_pop",
#         base_gate=base_gate,
#         and_gates=and_gates,
#         not_gates=not_gates,
#         or_gates=or_gates,
#         xor_gates=xor_gates,
#     )
# test_all_population_properties(complex_pop)


@responses.activate
def test_create_complex_population(experiment, gates, populations):
    complex_pop = experiment.create_complex_population(
        {
            "$and": [
                gates[0]["_id"],
                gates[1]["_id"],
                {"$or": [gates[2]["_id"], gates[3]["_id"]]},
            ]
        }
    )

    test_all_population_properties(complex_pop)
