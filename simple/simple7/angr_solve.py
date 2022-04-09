import angr
import sys

import claripy

fail = 0x4015BC
success = 0x4015EB


project = angr.Project('./simple7.exe')

start_addr = 0x40151F
initial_state: angr.SimState = project.factory.blank_state(
    addr=start_addr,
    add_options={
        angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
    }
)

flag = [claripy.BVS(f'f%d' % i, 8) for i in range(19)]


initial_state.regs.rbp = initial_state.regs.rsp
initial_state.regs.rbp += 0xa0

for i in range(len(flag) - 1):
    initial_state.add_constraints(flag[i] >= 32)
    initial_state.add_constraints(flag[i] < 127)
    initial_state.memory.store(initial_state.regs.rbp - 0x80 + i, flag[i])
initial_state.add_constraints(flag[-1] == 0)

simgr = project.factory.simgr(initial_state)

from timeit import default_timer
start = default_timer()
simgr.explore(find=success, avoid=fail)
print(f'explore elapsed time: {default_timer() - start}s')
if simgr.found:
    print('found')
    state = simgr.found[0]
    print(bytes([state.solver.eval(flag[i]) for i in range(len(flag))]))

else:
    print('solution not found')
