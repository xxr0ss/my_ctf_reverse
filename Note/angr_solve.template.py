import angr
import sys
import claripy


project = angr.Project(sys.argv[1])

start_addr = 0x400010
initial_state = project.factory.blank_state(
    addr=start_addr,
    add_options={
        angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
    }
)


"""
假如有必要自己创建符号用于执行, 在这里创建, 在simgr生成前, 将符号存放进initial_state
"""
flag = [claripy.BVS(f'f%d' % i, 8) for i in range(19)]

"""
我们假定flag由可见字符组成
将我们创建的符号放入我们设置好的栈上
"""
# 分配栈空间，怎么给rbp，rsp赋值，取决于这个时候，statte.regs里这两个寄存器是符号值还是
# 确定的值。可以写个print看下，本例中一开始rbp是符号，rsp是个确定的值，所以写如下代码
# 实现栈的构造。
initial_state.regs.rbp = initial_state.regs.rsp
initial_state.regs.rbp += 0xa0
for i in range(len(flag) - 1):
    initial_state.add_constraints(flag[i] >= 32)
    initial_state.add_constraints(flag[i] < 127)
    initial_state.memory.store(initial_state.regs.rbp - 0x80 + i, flag[i])
initial_state.add_constraints(flag[-1] == 0)


simgr = project.factory.simgr(initial_state)

"""
参照原文档
The "find" and "avoid" parameters may be any of:

- An address to find
- A set or list of addresses to find
- A function that takes a state and returns whether or not it matches.
"""
simgr.explore(
    find=0x400080,
    avoid=0x40090
)


if simgr.found:
    # 如果simgr找到合适的路径，我们就来evaluate一下flag中的符号的值。
    print('found')
    state = simgr.found[0]
    print(bytes([state.solver.eval(flag[i]) for i in range(len(flag))]))

else:
    print('solution not found')
