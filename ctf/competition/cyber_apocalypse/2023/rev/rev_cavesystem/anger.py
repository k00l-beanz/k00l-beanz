#!/usr/bin/env python3

import angr

project = angr.Project("./cave", auto_load_libs=False)

@project.hook(0x401aba)
def print_flag(state):
    print("flag: ", state.posix.dumps(0))
    project.terminate_execution()

project.execute()