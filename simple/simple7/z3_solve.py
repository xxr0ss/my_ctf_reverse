from z3 import *


solver = Solver()


flag = [BitVec(f'f{i}', 8) for i in range(18)]


for i in range(len(flag)):
    solver.add(flag[i] > 32)
    solver.add(flag[i] < 127)

cmp_data = [160, 230, 122, 286, 230, 144, 290, 208, 240, 144, 300, 216, 290, 244, 240, 100, 256, 310]

for i in range(len(flag)):
    # v3 = (flag[i] >> 7) >> 4
    a = (flag[i] >> 4) & 0xF
    # v4 = ((16 * flag[i]) >> 31) >> 28
    b = (((16 * flag[i]) >> 4)) & 0xF
    c = 22 * a + 12 * b
    solver.add(c == cmp_data[i])


if str(solver.check()) == 'sat':
    model = solver.model()
    flag = bytes([model[byte].as_long() for byte in flag])
    print(flag.decode())
else:
    print('unsat')