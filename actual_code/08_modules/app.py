import cern.utils as ut
from cern.utils import Shape as S, triangle, add
from cern.user_functions import find_user_by_email
from cern import find_user_by_email

# import numpy as np
# import pandas as pd
# name-spaced 
print(ut.add(1,2))

circle = ut.Shape("circle")
print(circle.type)

print(ut.triangle.type)

parallelogram = S("parallelogram")

print("=" * 10, "app.py", "=" * 10)
print(__name__)
print(__file__)
print(__doc__)
print("=" * 27)
print("=" * 10, "utils from app.py", "=" * 10)
print(ut.__name__)
print(ut.__file__)
print(ut.__doc__)
print([o for o in dir(ut) if not o.startswith("_")])
print("=" * 27)