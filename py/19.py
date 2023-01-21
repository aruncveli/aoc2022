from dataclasses import dataclass
from enum import Enum, auto
from itertools import accumulate

from parse import parse  # type: ignore


class Robot(Enum):
    ORE = auto()
    CLAY = auto()
    OBSIDIAN = auto()
    GEODE = auto()


@dataclass
class Part:
    number: int
    time_limit: int
    blueprints_limit: int


parts = (Part(1, 24, 0), Part(2, 32, 3))


def calculate(part: Part) -> int:
    max_possible_items_per_minute = tuple(
        accumulate(
            range(part.time_limit + 1)
        )
    )

    if part.number == 1:
        quality_level = 0
    else:
        quality_level = 1

    with open('../input/19') as file:
        blueprint_num: int
        ore_robot_ore_cost: int
        clay_robot_ore_cost: int
        obsidian_robot_ore_cost: int
        obsidian_robot_clay_cost: int
        geode_robot_ore_cost: int
        geode_robot_obsidian_cost: int

        for blueprint in file:
            blueprint_num, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, \
                geode_robot_ore_cost, geode_robot_obsidian_cost = parse(
                'Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot '
                'costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.\n', blueprint)

            max_ore_cost = max(ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, geode_robot_ore_cost)

            max_geodes = 0

            def update_max_geodes(time_remaining: int, robot_type: Robot, num_ore_robots: int, num_clay_robots: int,
                                  num_obsidian_robots: int, num_geode_robots: int, ores: int, clays: int,
                                  obsidians: int,
                                  geodes: int) -> None:

                nonlocal max_geodes

                if robot_type == Robot.ORE and num_ore_robots >= max_ore_cost \
                        or robot_type == Robot.CLAY and num_clay_robots >= obsidian_robot_clay_cost \
                        or robot_type == Robot.OBSIDIAN and (
                        num_obsidian_robots >= geode_robot_obsidian_cost or num_clay_robots == 0) \
                        or robot_type == Robot.GEODE and num_obsidian_robots == 0 \
                        or geodes + num_geode_robots * time_remaining + max_possible_items_per_minute[
                    time_remaining] <= max_geodes:
                    return

                while time_remaining:
                    if robot_type == Robot.ORE and ores >= ore_robot_ore_cost:
                        for robot_type in Robot:
                            update_max_geodes(time_remaining - 1, robot_type, num_ore_robots + 1, num_clay_robots,
                                              num_obsidian_robots, num_geode_robots,
                                              ores - ore_robot_ore_cost + num_ore_robots, clays + num_clay_robots,
                                              obsidians + num_obsidian_robots, geodes + num_geode_robots)
                        return
                    elif robot_type == Robot.CLAY and ores >= clay_robot_ore_cost:
                        for robot_type in Robot:
                            update_max_geodes(time_remaining - 1, robot_type, num_ore_robots, num_clay_robots + 1,
                                              num_obsidian_robots, num_geode_robots,
                                              ores - clay_robot_ore_cost + num_ore_robots,
                                              clays + num_clay_robots, obsidians + num_obsidian_robots,
                                              geodes + num_geode_robots)
                        return
                    elif robot_type == Robot.OBSIDIAN and ores >= obsidian_robot_ore_cost and clays >= obsidian_robot_clay_cost:
                        for robot_type in Robot:
                            update_max_geodes(time_remaining - 1, robot_type, num_ore_robots, num_clay_robots,
                                              num_obsidian_robots + 1, num_geode_robots,
                                              ores - obsidian_robot_ore_cost + num_ore_robots,
                                              clays - obsidian_robot_clay_cost + num_clay_robots,
                                              obsidians + num_obsidian_robots,
                                              geodes + num_geode_robots)
                        return
                    elif robot_type == Robot.GEODE and ores >= geode_robot_ore_cost and obsidians >= geode_robot_obsidian_cost:
                        for robot_type in Robot:
                            update_max_geodes(time_remaining - 1, robot_type, num_ore_robots, num_clay_robots,
                                              num_obsidian_robots, num_geode_robots + 1,
                                              ores - geode_robot_ore_cost + num_ore_robots,
                                              clays + num_clay_robots,
                                              obsidians - geode_robot_obsidian_cost + num_obsidian_robots,
                                              geodes + num_geode_robots)
                        return

                    time_remaining -= 1
                    ores += num_ore_robots
                    clays += num_clay_robots
                    obsidians += num_obsidian_robots
                    geodes += num_geode_robots

                max_geodes = max(max_geodes, geodes)

            for robot_type in Robot:
                update_max_geodes(part.time_limit, robot_type, 1, 0, 0, 0, 0, 0, 0, 0)

            if part.number == 1:
                quality_level += blueprint_num * max_geodes
            else:
                quality_level *= max_geodes
                if blueprint_num == part.blueprints_limit:
                    break
        return quality_level


print('Part 1:', calculate(Part(1, 24, 0)))
print('Part 2:', calculate(Part(2, 32, 3)))
