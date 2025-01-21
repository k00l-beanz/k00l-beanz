#!/usr/bine/env python3

import angr
import claripy

# Declare project
BINARY = "./spookylicence"
BASE_ADDRESS = 0x100000
project = angr.Project(BINARY,
                       main_opts={"base_addr":BASE_ADDRESS},
                       auto_load_libs=True)

# Declare the symbolic variable 'flag'
flag = claripy.BVS("flag", 8 * 32)
claripy.BVV('A')

# Initialize the state
state = project.factory.full_init_state(args=[BINARY, flag],
                                        add_options=angr.options.unicorn)

# Create the simulator manager
sim_manager = project.factory.simulation_manager(state)
sim_manager.explore(find=0x0010187d)

# Check if any path was found
if len(sim_manager.found) > 0:
    print(sim_manager.found[0].solver.eval(flag, cast_to=bytes))