from sympy import *

l1, l2 = var("l1 l2", positive=True)
dl1, dl2 = var("dl1 dl2", positive=True)
z1, z2 = var("z1 z2", real=True)
q1, q2 = var("q1 q2", real=True)

x = (l1) * cos(q1 + dl1*z1) + (l2) * cos(q1 + dl1*z1 + q2 + dl2*z2)
y = (l1) * sin(q1 + dl1*z1) + (l2) * sin(q1 + dl1*z1 + q2 + dl2*z2)

pxpq1 = x.diff(q1)
pxpq2 = x.diff(q2)
pypq1 = y.diff(q1)
pypq2 = y.diff(q2)

J = Matrix([[pxpq1, pxpq2],
            [pypq1, pypq2]])

M = sqrt(det(J * J.T))

from pathlib import Path

with open(Path(__file__).parent / "equations.txt", "w") as ef:
    for n in ["x", "y", "pxpq1", "pxpq2", "pypq1", "pypq2", "J", "M"]:
        print("{} = {}".format(n, eval(n)), file=ef)
        print("{} = {}".format(n, eval(n)))
