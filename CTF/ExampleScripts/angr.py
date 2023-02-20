#!/usr/bin/env python3

# Angr Documentation: https://docs.angr.io/
# To start, init the Python virtual environment:
# 	/usr/share/virtualenvwrapper/virtualenvwrapper.sh --python=$(which python3) angr && pip install angr


import angr

# Load ctfd_plus and specify the base address. auto_load_libs prevents angr from loading
# libraries the main program depends upon
project = angr.Project("./vuln", main_opts={"base_addr":0}, auto_load_libs=False)

# Creates an initial program state for the Angr simulation
initial_state = project.factory.entry_state()
print(initial_state)

# Creates a simulation manager object that will manage the exploration of the program state
sm = project.factory.simgr(initial_state)

# Addresses
target_address = 0x0112E
avoid_address = 0x01117

# Runs the simulation exploring different paths through the program unjtil it reaches the target address
sm.explore(find=target_address, avoid=avoid_address)

print(sm)
print(sm.found[0].posix.dumps(0))
