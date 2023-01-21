from functools import cache
from typing import Any

from networkx import DiGraph, all_pairs_shortest_path_length  # type: ignore
from parse import parse  # type: ignore

G = DiGraph()
with open('../input/16') as file:
    source: str
    flow_rate: int
    targets_spec: str
    targets: list[str]

    for line in file:
        source, flow_rate, targets_spec = parse('Valve {} has flow rate={:d}; {}\n', line)
        for i in range(len(targets_spec)):
            if targets_spec[i].isupper():
                targets = targets_spec[i:].split(', ')
                break

        G.add_node(source, flow_rate=flow_rate)
        for target in targets:
            G.add_edge(source, target)

time_to_move = dict(all_pairs_shortest_path_length(G))
valves = frozenset(G)


@cache
def find_max_pressure(time_left: int, source: str, valves: frozenset[Any], with_elephant: bool) -> int:
    max_pressure = 0
    for valve in valves:
        if G.nodes[valve]['flow_rate'] and time_to_move[source][valve] < time_left:
            # Target valve can be opened
            time_left_for_valve = time_left - time_to_move[source][valve] - 1
            pressure_released_by_current_valve = G.nodes[valve]['flow_rate'] * time_left_for_valve
            pressure_released_by_succeeding_valves = find_max_pressure(time_left_for_valve, valve, valves - {valve},
                                                                       with_elephant)
            pressure_released_by_elephant = find_max_pressure(26, 'AA', valves, False) if with_elephant else 0

            max_pressure = max(max_pressure,
                               pressure_released_by_current_valve + pressure_released_by_succeeding_valves,
                               pressure_released_by_elephant)
    return max_pressure


print('Part 1:', find_max_pressure(30, 'AA', valves, False))
print('Part 2:', find_max_pressure(26, 'AA', valves, True))
