#!/usr/bin/env python3
# k00l-beanz

import angr
import claripy

# Declare a project
BINARY = "./tablet"
BASE_ADDRESS = 0x100000
DEST_ADDRESS = 0x00101371
project = angr.Project(BINARY,
                       main_opts={"base_addr":BASE_ADDRESS},
                       auto_load_libs=True)

# Declare the symoblic variable 'flag'
flag = claripy.BVS("flag", 8 * 64)
claripy.BVV('A')

# Initialize the state
state = project.factory.full_init_state(args=[BINARY], 
                                        add_options=angr.options.unicorn, 
                                        stdin=flag)

# Create the simulator manager
sim_manager = project.factory.simulation_manager(state)
sim_manager.explore(find=DEST_ADDRESS)

# Check if any path was found
if len(sim_manager.found) > 0:
    print(sim_manager.found[0].solver.eval(flag, cast_to=bytes))